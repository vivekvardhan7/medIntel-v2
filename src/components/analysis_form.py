import streamlit as st
from services.ai_service import generate_analysis
from config.prompts import SPECIALIST_PROMPTS
from utils.pdf_extractor import extract_text_from_pdf
from config.sample_data import SAMPLE_REPORT
from config.app_config import MAX_UPLOAD_SIZE_MB

def show_analysis_form():
    if 'current_session' in st.session_state and 'report_source' not in st.session_state:
        st.session_state.report_source = "Upload PDF"
    
    report_source = st.radio(
        "Choose report source",
        ["Upload PDF", "Use Sample PDF"],
        index=0 if st.session_state.get('report_source') == "Upload PDF" else 1,
        horizontal=True,
        key='report_source'
    )

    pdf_contents = get_report_contents(report_source)
            
    if pdf_contents:
        render_patient_form(pdf_contents)

def get_report_contents(report_source):
    if report_source == "Upload PDF":
        uploaded_file = st.file_uploader(
            f"Upload blood report PDF (Max {MAX_UPLOAD_SIZE_MB}MB)", 
            type=['pdf'],
            help=f"Maximum file size: {MAX_UPLOAD_SIZE_MB}MB. Only PDF files containing medical reports are supported"
        )
        if uploaded_file:
            file_size_mb = uploaded_file.size / (1024 * 1024)
            if file_size_mb > MAX_UPLOAD_SIZE_MB:
                st.error(f"File size ({file_size_mb:.1f}MB) exceeds the {MAX_UPLOAD_SIZE_MB}MB limit.")
                return None
                
            if uploaded_file.type != 'application/pdf':
                st.error("Please upload a valid PDF file.")
                return None
                
            pdf_contents = extract_text_from_pdf(uploaded_file)
            if isinstance(pdf_contents, str) and (
                pdf_contents.startswith(("File size exceeds", "Invalid file type", "Error validating")) or
                pdf_contents.startswith("The uploaded file") or
                "error" in pdf_contents.lower()
            ):
                st.error(pdf_contents)
                return None
            with st.expander("📄 View Extracted Report"):
                st.text(pdf_contents)
            return pdf_contents
    else:
        with st.expander("📄 View Sample Report"):
            st.text(SAMPLE_REPORT)
        return SAMPLE_REPORT
    return None

def render_patient_form(pdf_contents):
    with st.form("analysis_form"):
        st.markdown("### 🧑‍⚕️ Patient Information")
        patient_name = st.text_input("Patient Name")
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=0, max_value=120)
        with col2:
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        
        submitted = st.form_submit_button("🔍 Analyze Report")
        if submitted:
            handle_form_submission(patient_name, age, gender, pdf_contents)

def handle_form_submission(patient_name, age, gender, pdf_contents):
    if not all([patient_name, age, gender]):
        st.error("❗ Please fill in all fields")
        return

    can_analyze, error_msg = generate_analysis(None, None, check_only=True)
    if not can_analyze:
        st.error(error_msg)
        st.stop()
        return

    with st.spinner("🔎 Analyzing report using AI..."):
        st.session_state.auth_service.save_chat_message(
            st.session_state.current_session['id'],
            f"Analyzing report for patient: {patient_name}"
        )

        result = generate_analysis({
            "patient_name": patient_name,
            "age": age,
            "gender": gender,
            "report": pdf_contents
        }, SPECIALIST_PROMPTS["comprehensive_analyst"])

    if result["success"]:
        content = result["content"]

        # Optional model info
        if "model_used" in result:
            content += f"\n\n---\n📌 *Generated using `{result['model_used']}`*"

        # Save to history
        st.session_state.auth_service.save_chat_message(
            st.session_state.current_session['id'],
            content,
            role='assistant'
        )

        # ✅ Display the result on screen
        st.success("✅ Analysis complete!")
        st.markdown(content, unsafe_allow_html=True)

    else:
        st.error(result["error"])
