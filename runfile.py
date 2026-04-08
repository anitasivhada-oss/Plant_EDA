import streamlit as st
import pandas as pd
 
# Optional profiling libraries

import sweetviz as sv

st.set_page_config(page_title="EDA Workshop App", layout="wide")

st.title("📊 EDA Workshop - Streamlit App")
st.write("Upload your dataset and perform exploratory data analysis.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Read dataset
    df = pd.read_csv(uploaded_file, sep=';')

    st.subheader("🔍 Data Preview")
    st.write(df.head())

    st.subheader("🔚 Last Rows")
    st.write(df.tail())

    st.subheader("📈 Descriptive Statistics")
    st.write(df.describe())

    st.subheader("ℹ️ Data Info")
    buffer = []
    df.info(buf=buffer)
    s = "\n".join(buffer)
    st.text(s)

    st.subheader("❗ Missing Values")
    st.write(df.isnull().sum())

    # YData Profiling Report
    st.subheader("📊 Profiling Report (ydata_profiling)")
    if st.button("Generate Profiling Report"):
        profile = ProfileReport(df, title="CombinedTraits", explorative=True)
        profile.to_file("profile_report.html")
        with open("profile_report.html", "r", encoding="utf-8") as f:
            st.components.v1.html(f.read(), height=800, scrolling=True)

    # Sweetviz Report
    st.subheader("🍭 Sweetviz Report")
    if st.button("Generate Sweetviz Report"):
        report = sv.analyze(df)
        report.show_html("sweetviz_report.html")
        with open("sweetviz_report.html", "r", encoding="utf-8") as f:
            st.components.v1.html(f.read(), height=800, scrolling=True)

else:
    st.info("Please upload a CSV file to begin.")
