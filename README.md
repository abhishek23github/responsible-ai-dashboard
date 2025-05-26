# 🤖 Responsible AI & LLM Evaluation Dashboard

A Streamlit-based tool to evaluate LLM-generated outputs across key Responsible AI metrics like **Toxicity**, **Bias**, **Accuracy**, **Relevance**, and **Coherence**.

---

## 🚀 Features

- ✍️ Prompt interface with OpenAI (gpt-3.5 / gpt-4)
- ✅ Evaluation on 5 key metrics
- 📊 Interactive dashboard (histograms, trends, comparisons)
- ⚠️ Real-time alerting for problematic outputs
- 📁 Export full logs & flagged entries to CSV

---

## 🖼️ UI Preview

| Prompt Panel | Dashboard |
|--------------|-----------|
| ![Prompt](./screenshots/ui.png) | ![Dashboard](./screenshots/dashboard.png) |

---

## 🛠 Tech Stack

| Layer          | Tool / Library           |
|----------------|--------------------------|
| Frontend UI     | Streamlit                |
| LLM API         | OpenAI (`openai` lib)    |
| Toxicity        | Perspective API (or Detoxify) |
| Bias Detection  | Keyword scan             |
| Accuracy/Etc.   | Simulated                |
| Visualization   | Matplotlib               |
| Logging         | Pandas → CSV             |

---

## 📂 Project Structure

```bash
├── app/
│   ├── toxicity_eval.py
│   ├── bias_eval.py
│   └── general_eval.py
├── ui/
│   ├── ui_streamlit.py   # Prompt + scoring UI
│   └── visualize.py      # Full dashboard & export
├── data/
│   └── logs.csv          # Generated score logs
├── requirements.txt
├── .env.template         # Add OpenAI key
├── launch_dashboard.bat  # Optional one-click launcher
└── README.md
```

---

## 🔧 Installation

```bash
git clone https://github.com/your-name/responsible-ai-dashboard.git
cd responsible-ai-dashboard
python -m venv venv
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
# Run UI (port 8501)
streamlit run ui/ui_streamlit.py

# Run Dashboard (port 8502 in separate terminal)
streamlit run ui/visualize.py --server.port 8502
```

---

## 📁 Environment Setup

Copy `.env.template` to `.env` and add your key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxx
```

---

## 📤 Deployment (Optional)

✅ GitHub-ready  
🌐 Deployable to [Streamlit Cloud](https://streamlit.io/cloud) or locally via `.bat`

---

## 🪪 License

MIT License — free to use for learning, auditing & responsible testing.