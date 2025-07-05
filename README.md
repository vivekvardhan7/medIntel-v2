# 🩺 MedIntel — AI-Powered Health Report Analyst

**MedIntel** is a next-generation medical intelligence platform powered by Groq's LLMs, capable of extracting and interpreting blood reports in real-time. With a modular agent system and adaptive model fallback mechanism, MedIntel delivers personalized, context-aware health insights in seconds.

<p align="center">
  <img src="https://img.shields.io/badge/Built_with-Streamlit-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Powered_by-Groq_Models-purple?style=flat-square"/>
  <img src="https://img.shields.io/github/license/vivekvardhan7/medIntel-v2?style=flat-square"/>
  <img src="https://img.shields.io/badge/Made%20with-%F0%9F%92%96%20by%20Sai%20Vivek%20Vardhan-blueviolet?style=flat-square"/>
</p>

---

## ⚡ Core Features

- 🧠 **Multi-Agent Architecture** – LLM agents communicate in a cascaded system to generate accurate, medically sound insights.
- 📑 **Medical PDF Parsing (up to 20MB)** – Upload health reports and extract structured, readable data.
- 🔐 **User Auth & Session Memory** – Supabase-secured authentication with session history, allowing repeatable and contextual analysis.
- 🔄 **AI Fallback Mechanism** – Automatically switches between Groq-powered models for performance and cost-efficiency.
- 📊 **Insightful Health Feedback** – Personalized recommendations, summaries, and red-flag indicators in layman-friendly language.
- 🎨 **Modern Streamlit UI** – Fast, mobile-friendly, real-time interface with modular components.

---

## 🧠 Tech Stack Overview

| Layer        | Technology                                                   |
|-------------|---------------------------------------------------------------|
| UI/Frontend | Streamlit (Modular Components)                                |
| Auth        | Supabase Auth (Email-based secure auth)                       |
| Database    | Supabase PostgreSQL                                           |
| AI Models   | Groq-hosted LLaMA-3 70B, 8B, Mixtral, and fallback Gemma-7B   |
| PDF Parsing | PDFPlumber                                                    |
| Orchestration | Python (Agent-based coordination, fallback handling)        |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- Groq API Key
- Supabase project (URL + API key)
- Streamlit v1.30.0+
- PDFPlumber

### 🧪 Installation

```bash
git clone https://github.com/vivekvardhan7/medIntel-v2.git
cd medIntel-v2
pip install -r requirements.txt


🗂 Project Structure
csharp
Copy
Edit
medIntel-v2/
├── src/
│   ├── main.py               # 🔁 Streamlit app entrypoint
│   ├── auth/
│   │   ├── auth_service.py   # 🔐 Supabase integration
│   │   └── session_manager.py
│   ├── components/
│   │   ├── analysis_form.py
│   │   ├── auth_pages.py
│   │   ├── sidebar.py
│   │   └── footer.py
│   ├── config/
│   │   ├── app_config.py
│   │   └── prompts.py        # 🧠 Custom AI prompt design
│   ├── services/
│   │   └── ai_service.py     # 🔌 Groq + LLM coordination
│   ├── agents/
│   │   ├── agent_manager.py
│   │   └── model_fallback.py
│   └── utils/
│       ├── validators.py
│       └── pdf_extractor.py
├── .streamlit/
│   └── secrets.toml
├── public/
│   └── db/
│       ├── schema.png
│       └── script.sql
├── requirements.txt
├── README.md
└── LICENSE
🎯 Usage
bash
Copy
Edit
streamlit run src/main.py
Once running, you'll be able to:

Login/Signup securely

Upload a PDF health report

Receive AI-analyzed health feedback

View session summaries and revisit past uploads

🤝 Contributions
We welcome all contributions — feature ideas, bug fixes, docs, UI polish, and more.

Please check out CONTRIBUTING.md for how to get started.

👨‍💻 Maintainer
Name	GitHub	Role
Sai Vivek Vardhan	@vivekvardhan7	Creator & Maintainer

📄 License
Licensed under the MIT License. Use it, fork it, build on top of it!

🌐 Deployment (Coming Soon)
Planned support for:

Streamlit Cloud / HuggingFace Spaces

Render / Railway

Docker containerization

yaml
Copy
Edit

---

Would you like me to:

- Add a **project banner or logo** to the top?
- Auto-generate `requirements.txt` based on your `src/` folder?
- Add a `Dockerfile` or `Streamlit Cloud` deployment workflow?

Let me know how deep you want to go!