import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Financial Marketing Dashboard")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(data.head())

    column = st.selectbox("Select column", data.columns)

    if data[column].dtype == 'object':
        pie_data = data[column].value_counts().head(10)
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
        st.pyplot(fig)
    else:
        st.line_chart(data[column])
else:
    st.warning("Upload a CSV file")
