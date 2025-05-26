# 🧱 High-Level Design: Responsible AI Evaluation Dashboard

---

## 🎯 Objective

To build a responsible AI evaluation system that allows developers to:

- Prompt LLMs (like ChatGPT)
- Score the output using Responsible AI metrics
- Alert if any metric fails
- Store results
- Visualize trends, comparisons, and flags

---

## ⚙️ Core Components

### 1. 🧾 Prompt Evaluator (`ui/ui_streamlit.py`)

- Prompt entry
- Model selection
- Calls OpenAI API
- Calculates:
  - Toxicity (Perspective API)
  - Bias (keyword scan)
  - Accuracy, Relevance, Coherence (simulated or GPT-based)
- Logs to CSV
- Displays real-time alerts

---

### 2. 🧠 Evaluators (`app/`)

| File                  | Purpose                     |
|-----------------------|-----------------------------|
| `toxicity_eval.py`    | Sends to Perspective API    |
| `bias_eval.py`        | Keyword-based bias scan     |
| `general_eval.py`     | Simulates accuracy metrics  |

---

### 3. 📊 Dashboard (`ui/visualize.py`)

- Reads CSV log
- Shows:
  - Histograms for each metric
  - Time trend (toxicity over time)
  - Model-wise bar charts
  - Bias/Accuracy/Relevance/Coherence tabs
  - Export section for full and flagged logs

---

## 🧠 Architecture Diagram

```plaintext
+-------------+        +------------+      +---------------+
|   User UI   +------->+  OpenAI API+----->+LLM Response    |
+-------------+        +------+-----+      +-------+-------+
                                 |                  |
                                 v                  v
                        +--------+--------+ +-------+--------+
                        |  Metric Evaluators |-> log to CSV   |
                        +--------+--------+ +----------------+
                                 |
                                 v
                          +-------------+
                          | Dashboard UI|
                          +-------------+
```

---

## 📋 Data Flow

```plaintext
Prompt → LLM → Response
         ↓
   Metric Evaluation
         ↓
     CSV Logging
         ↓
     Visualization + Export
```

---

## 🔐 Security

- `.env` used to store OpenAI keys (not committed)
- Data stored locally (CSV only)
- No PII exposed or stored

---

## 📌 Future Enhancements

- PDF report generation
- GPT-based accuracy evaluator
- Streamlit Cloud deployment
- Admin panel with filters