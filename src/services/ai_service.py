import streamlit as st
from agents.analysis_agent import AnalysisAgent

def init_analysis_state():
    """Initialize analysis-related session state variables."""
    if 'analysis_agent' not in st.session_state:
        print("🔄 Initializing AnalysisAgent...")
        st.session_state.analysis_agent = AnalysisAgent()

def check_rate_limit():
    init_analysis_state()
    can_analyze, msg = st.session_state.analysis_agent.check_rate_limit()
    print(f"🟡 Rate limit check: {can_analyze}, Message: {msg}")
    return can_analyze, msg

def generate_analysis(data, system_prompt, check_only=False, session_id=None):
    """Generate analysis if within rate limits."""
    print("🚀 generate_analysis() called...")
    init_analysis_state()

    if check_only:
        print("⏸️ Only checking rate limit...")
        return st.session_state.analysis_agent.check_rate_limit()

    print("🧠 Preparing to analyze report...")
    try:
        result = st.session_state.analysis_agent.analyze_report(
            data=data,
            system_prompt=system_prompt,
            check_only=False
        )
        print("✅ AI Analysis result:", result)
        return result
    except Exception as e:
        print("❌ Exception occurred in generate_analysis():", e)
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "error": f"Internal error occurred during analysis: {str(e)}"
        }
