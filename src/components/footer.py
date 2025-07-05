import streamlit as st

def show_footer(in_sidebar=False):
    base_styles = f"""
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(to right, #0f172a, #1e293b);
        color: #e2e8f0;
        border-top: 1px solid #334155;
        margin-top: {'0' if in_sidebar else '2rem'};
        width: 100%;
        font-family: 'Segoe UI', sans-serif;
        font-size: 0.85rem;
    """

    st.markdown(
        f"""
        <div style="{base_styles}">
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span>Made by<span style="color:#f43f5e; font-size: 1rem;"></span> by</span>
                    <strong style="color: #38bdf8;"> Sai Vivek </strong>
                </div>
                <div style="opacity: 0.6;">© 2025 • NIT Mizoram • All rights reserved</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
