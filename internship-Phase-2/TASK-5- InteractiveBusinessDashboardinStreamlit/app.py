# Streamlit Business Dashboard - Global Superstore
import streamlit as st  # streamlit for dashboard
import pandas as pd
import matplotlib.pyplot as plt

st.title("Global Superstore Business Dashboard")  # dashboard title

df = pd.read_csv('Global_Superstore2.csv', encoding='latin1')  # loading data

# sidebar filters
region = st.sidebar.multiselect("Select Region", df['Region'].unique())  # region filter
category = st.sidebar.multiselect("Select Category", df['Category'].unique())  # category filter
subcat = st.sidebar.multiselect("Select Sub-Category", df['Sub-Category'].unique())  # sub-category filter

# applying filters
filtered = df.copy()
if region: filtered = filtered[filtered['Region'].isin(region)]
if category: filtered = filtered[filtered['Category'].isin(category)]
if subcat: filtered = filtered[filtered['Sub-Category'].isin(subcat)]

# KPIs
col1, col2 = st.columns(2)  # two columns for KPIs
col1.metric("Total Sales", f"${filtered['Sales'].sum():,.0f}")  # total sales KPI
col2.metric("Total Profit", f"${filtered['Profit'].sum():,.0f}")  # total profit KPI

# top 5 customers chart
st.subheader("Top 5 Customers by Sales")
top5 = filtered.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)
st.bar_chart(top5)  # displaying bar chart

# sales by category chart
st.subheader("Sales by Category")
st.bar_chart(filtered.groupby('Category')['Sales'].sum())
