import streamlit as st
import random
import pandas as pd

# --------------------------
# App title and description
# --------------------------
st.set_page_config(page_title="AI Credit Risk Assessment", layout="centered")
st.title("🏦 AI Credit Risk Assessment")
st.subheader("Prototype Dashboard - Hackathon Version")
st.write("Enter your information below and see a risk analysis immediately.")

# --------------------------
# Layout: two columns for structured inputs
# --------------------------
col1, col2 = st.columns(2)

with col1:
    income = st.number_input("Monthly Income", min_value=0, step=100)
    age = st.number_input("Age", min_value=18, max_value=100)
with col2:
    debt_ratio = st.number_input("Debt-to-Income Ratio", min_value=0.0, max_value=1.0, step=0.01)
    employment = st.selectbox("Employment Status", ["Employed", "Self-Employed", "Unemployed"])

# --------------------------
# Text input for LLM analysis
# --------------------------
with st.expander("Additional Info (LLM Analysis)"):
    credit_text = st.text_area("Reason for Loan / Customer Message")

# --------------------------
# Predict button
# --------------------------
if st.button("Predict Risk"):

    # --------------------------
    # Dummy risk score (replace later with ML + LLM)
    # --------------------------
    risk_score = round(random.uniform(0, 1), 2)

    # Determine risk level with colors and emojis
    if risk_score < 0.4:
        risk_level = "<span style='color:green'>Low Risk 🟢</span>"
    elif risk_score < 0.7:
        risk_level = "<span style='color:orange'>Medium Risk 🟡</span>"
    else:
        risk_level = "<span style='color:red'>High Risk 🔴</span>"

    # --------------------------
    # Display results
    # --------------------------
    st.subheader("Prediction Result")
    st.write(f"Risk Score: {risk_score}")
    st.markdown(f"Risk Level: {risk_level}", unsafe_allow_html=True)

    # Dummy LLM explanation placeholder
    st.write("LLM Analysis: This is a placeholder explanation. Real explanation will come from LLM + ML model.")

    # --------------------------
    # Bar chart of risk factors
    # --------------------------
    factor_data = pd.DataFrame({
        "Factor": ["Income", "Debt Ratio", "Age"],
        "Score": [income/10000, debt_ratio, age/100]
    })
    st.subheader("Risk Factors Overview")
    st.bar_chart(factor_data.set_index("Factor"))
