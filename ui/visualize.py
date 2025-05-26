import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Responsible AI Dashboard", layout="wide")
st.title("📊 Responsible AI Evaluation Dashboard")

log_path = "data/logs.csv"

if not os.path.exists(log_path):
    st.warning("Log file not found. Please generate some prompts using the main app.")
else:
    df = pd.read_csv(log_path, on_bad_lines="skip")

    if "toxicity" not in df.columns:
        st.warning("No toxicity scores found. Run some prompts first.")
    else:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.dropna(subset=["timestamp"])
        df = df.sort_values("timestamp")
        df["rolling_avg"] = df["toxicity"].rolling(window=3, min_periods=1).mean()

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📊 Toxicity Histogram",
            "🏷️ Model Comparison",
            "📈 Toxicity Trend",
            "🧠 Bias Analysis",
            "📘 General Quality Metrics",
            "📤 Export / Reports"
        ])

        # TOXICITY HISTOGRAM
        with tab1:
            st.subheader("Toxicity Score Histogram")

            avg = df["toxicity"].mean()
            max_score = df["toxicity"].max()
            st.markdown(
                f"**Average Toxicity:** {avg:.2f} &nbsp;&nbsp;&nbsp;&nbsp; "
                f"**Max Toxicity:** {max_score:.2f}",
                unsafe_allow_html=True
            )

            fig, ax = plt.subplots(figsize=(6, 3.5))
            ax.hist(df["toxicity"], bins=10, range=(0, 1), color="skyblue", edgecolor="black")
            ax.set_xlabel("Toxicity Score")
            ax.set_ylabel("Frequency")
            ax.set_title("Distribution of Toxicity Scores")
            st.pyplot(fig)

        # MODEL COMPARISON (TOXICITY)
        with tab2:
            st.subheader("Average Toxicity by Model")

            if "model" in df.columns:
                model_scores = df.groupby("model")["toxicity"].mean().sort_values()
                st.markdown(f"**Models Compared:** {len(model_scores)}")

                fig2, ax2 = plt.subplots(figsize=(6, 3.5))
                model_scores.plot(kind="bar", color="mediumseagreen", ax=ax2)
                ax2.set_ylabel("Avg Toxicity Score")
                ax2.set_title("Model-wise Toxicity")
                st.pyplot(fig2)
            else:
                st.warning("No 'model' column found.")

        # TOXICITY TREND
        with tab3:
            st.subheader("Toxicity Trend Over Time")
            st.markdown("Showing rolling average with window size = 3 for smoothing.")

            fig3, ax3 = plt.subplots(figsize=(6, 3.5))
            ax3.plot(df["timestamp"], df["rolling_avg"], marker='o', linestyle='-')
            ax3.set_xlabel("Timestamp")
            ax3.set_ylabel("Toxicity (Rolling Avg)")
            ax3.set_title("Toxicity Trend Over Time")
            fig3.autofmt_xdate()
            st.pyplot(fig3)

        # BIAS ANALYSIS
        with tab4:
            st.subheader("🧠 Bias Analysis")

            if "bias" not in df.columns:
                st.warning("No bias scores found. Please generate new responses.")
            else:
                subtab1, subtab2 = st.tabs(["📊 Bias Histogram", "🏷️ Model-wise Bias"])

                with subtab1:
                    st.markdown("### 📊 Distribution of Bias Scores")
                    bias_avg = df["bias"].mean()
                    bias_max = df["bias"].max()
                    st.markdown(
                        f"**Average Bias Score:** {bias_avg:.2f} &nbsp;&nbsp;&nbsp;&nbsp; "
                        f"**Max Bias Score:** {bias_max:.2f}",
                        unsafe_allow_html=True
                    )

                    fig_b, ax_b = plt.subplots(figsize=(6, 3.5))
                    ax_b.hist(df["bias"], bins=10, range=(0, 1), color="salmon", edgecolor="black")
                    ax_b.set_xlabel("Bias Score")
                    ax_b.set_ylabel("Frequency")
                    ax_b.set_title("Bias Score Distribution")
                    st.pyplot(fig_b)

                with subtab2:
                    st.markdown("### 🧠 Model Comparison by Bias Score")

                    if "model" in df.columns:
                        model_bias = df.groupby("model")["bias"].mean().sort_values()

                        fig_bm, ax_bm = plt.subplots(figsize=(6, 3.5))
                        model_bias.plot(kind="bar", color="tomato", ax=ax_bm)
                        ax_bm.set_ylabel("Avg Bias Score")
                        ax_bm.set_title("Model-wise Average Bias")
                        st.pyplot(fig_bm)
                    else:
                        st.warning("No model data found.")

        # ACCURACY, RELEVANCE, COHERENCE
        with tab5:
            st.subheader("📘 Accuracy, Relevance, Coherence")

            if not all(col in df.columns for col in ["accuracy", "relevance", "coherence"]):
                st.warning("Not all quality metrics found. Please regenerate responses.")
            else:
                g1, g2, g3 = st.tabs(["✅ Accuracy", "🎯 Relevance", "🧠 Coherence"])

                # Accuracy
                with g1:
                    st.markdown("### ✅ Accuracy Score Distribution")
                    acc_avg = df["accuracy"].mean()
                    st.markdown(f"**Average Accuracy:** {acc_avg:.2f}")

                    fig_a, ax_a = plt.subplots(figsize=(6, 3.5))
                    ax_a.hist(df["accuracy"], bins=10, range=(0, 1), color="mediumblue", edgecolor="black")
                    ax_a.set_xlabel("Accuracy Score")
                    ax_a.set_ylabel("Frequency")
                    st.pyplot(fig_a)

                    st.markdown("### By Model")
                    acc_by_model = df.groupby("model")["accuracy"].mean()
                    fig_am, ax_am = plt.subplots(figsize=(6, 3.5))
                    acc_by_model.plot(kind="bar", color="steelblue", ax=ax_am)
                    ax_am.set_ylabel("Avg Accuracy")
                    st.pyplot(fig_am)

                # Relevance
                with g2:
                    st.markdown("### 🎯 Relevance Score Distribution")
                    rel_avg = df["relevance"].mean()
                    st.markdown(f"**Average Relevance:** {rel_avg:.2f}")

                    fig_r, ax_r = plt.subplots(figsize=(6, 3.5))
                    ax_r.hist(df["relevance"], bins=10, range=(0, 1), color="darkorange", edgecolor="black")
                    ax_r.set_xlabel("Relevance Score")
                    ax_r.set_ylabel("Frequency")
                    st.pyplot(fig_r)

                    st.markdown("### By Model")
                    rel_by_model = df.groupby("model")["relevance"].mean()
                    fig_rm, ax_rm = plt.subplots(figsize=(6, 3.5))
                    rel_by_model.plot(kind="bar", color="orange", ax=ax_rm)
                    ax_rm.set_ylabel("Avg Relevance")
                    st.pyplot(fig_rm)

                # Coherence
                with g3:
                    st.markdown("### 🧠 Coherence Score Distribution")
                    coh_avg = df["coherence"].mean()
                    st.markdown(f"**Average Coherence:** {coh_avg:.2f}")

                    fig_c, ax_c = plt.subplots(figsize=(6, 3.5))
                    ax_c.hist(df["coherence"], bins=10, range=(0, 1), color="seagreen", edgecolor="black")
                    ax_c.set_xlabel("Coherence Score")
                    ax_c.set_ylabel("Frequency")
                    st.pyplot(fig_c)

                    st.markdown("### By Model")
                    coh_by_model = df.groupby("model")["coherence"].mean()
                    fig_cm, ax_cm = plt.subplots(figsize=(6, 3.5))
                    coh_by_model.plot(kind="bar", color="mediumseagreen", ax=ax_cm)
                    ax_cm.set_ylabel("Avg Coherence")
                    st.pyplot(fig_cm)

        # EXPORT / REPORTS
        with tab6: 
            st.subheader("📤 Export Logs and Flagged Entries")

            if df.empty:
                st.warning("No logs available to export.")

            else:
                # Show download of full dataset 
                st.download_button(
                    label="📥 Download Full Log (CSV)",
                    data=df.to_csv(index=False).encode('utf-8'),
                    file_name="llm_log_full.csv",
                    mime="text/csv"
                )

            flagged_df = df[(df["toxicity"] > 0.7) | 
                            (df["bias"] > 0.5) | 
                            (df["accuracy"] < 0.7) | 
                            (df["relevance"] < 0.7) | 
                            (df["coherence"] < 0.7)
                            ]

            st.markdown(f"Flagged responses: **{len(flagged_df)}**")

            if not flagged_df.empty:
                st.download_button(
                    label="⚠️ Download Flagged Entries (CSV)",
                    data=flagged_df.to_csv(index=False).encode('utf-8'),
                    file_name="flagged_responses.csv",
                    mime="text/csv"
                )

                # optional preview 
                with st.expander("🔍 Preview Flagged Entries"):
                    st.dataframe(flagged_df)
                    
            else:
                st.success("✅ No flagged entries found. All responses are within safe limits.")
