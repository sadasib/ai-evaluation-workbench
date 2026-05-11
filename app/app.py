from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from evals.scoring import run_evaluation  # noqa: E402

st.set_page_config(page_title="AI Evaluation Workbench", layout="wide")

st.title("AI Evaluation Workbench")
st.caption("A product-focused way to evaluate GenAI response quality before launch.")

results = run_evaluation()

with st.sidebar:
    st.header("Filters")
    use_cases = sorted(results["use_case"].unique().tolist())
    selected_use_cases = st.multiselect("Use case", use_cases, default=use_cases)
    statuses = sorted(results["launch_status"].unique().tolist())
    selected_statuses = st.multiselect("Launch status", statuses, default=statuses)

filtered = results[
    results["use_case"].isin(selected_use_cases)
    & results["launch_status"].isin(selected_statuses)
]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Eval cases", len(filtered))
col2.metric("Average score", round(filtered["overall_score"].mean(), 2) if len(filtered) else "NA")
col3.metric("Pass", int((filtered["launch_status"] == "Pass").sum()))
col4.metric("Review", int((filtered["launch_status"] == "Review").sum()))

st.subheader("Score by use case")
if len(filtered):
    chart_df = filtered.groupby("use_case", as_index=False)["overall_score"].mean()
    fig = px.bar(chart_df, x="use_case", y="overall_score", range_y=[0, 5])
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No cases match the selected filters.")

st.subheader("Evaluation cases")
columns = [
    "case_id",
    "use_case",
    "risk_area",
    "user_query",
    "overall_score",
    "launch_status",
    "correctness",
    "policy_compliance",
    "escalation",
    "helpfulness",
    "safety",
]
st.dataframe(filtered[columns], use_container_width=True)

st.subheader("Case review")
case_ids = filtered["case_id"].tolist()
if case_ids:
    selected_case = st.selectbox("Select a case", case_ids)
    row = filtered[filtered["case_id"] == selected_case].iloc[0]

    st.markdown("#### User query")
    st.write(row["user_query"])

    st.markdown("#### Context")
    st.write(row["context"])

    st.markdown("#### Expected behavior")
    st.write(row["expected_behavior"])

    st.markdown("#### Model response")
    st.write(row["model_response"])

    st.markdown("#### PM interpretation")
    if row["launch_status"] == "Pass":
        st.success("This case meets the starter launch threshold.")
    else:
        st.warning("This case needs review before broader launch.")
else:
    st.info("Select filters that include at least one case.")

st.divider()
st.markdown(
    "This demo uses synthetic data and transparent heuristic scoring. "
    "It is designed as a portfolio artifact, not a production evaluation system."
)
