import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('all_df.csv')
st.set_page_config(page_title = 'US_Sale DashBoard 2025' , page_icon = ':bar_chart:', layout = 'wide')
st.sidebar.header('Please Filter Here')

product_name = st.sidebar.multiselect(
    'Select Product', 
    options = df['Product'].unique(),
    default = df['Product'].unique() [:5]
)

city_name = st.sidebar.multiselect(
    'Select City', 
    options = df['City'].unique(),
    default = df['City'].unique() [:5]
)

month_name = st.sidebar.multiselect(
    'Select Month', 
    options = df['Month'].unique(),
    default = df['Month'].unique() [:5]
)

st.title(':bar_chart: Sale Dashboard for 2019')
st.markdown('##')
total = df['Total'].sum()
n_product = df['Product'].nunique()
left_col , right_col = st.columns(2)
with left_col:
    st.subheader ('Total Sales')
    st.subheader (f"US $ {total}")
with right_col:
    st.subheader ('No. of Product')
    st.subheader (f"{n_product}")

df_select = df.query('City==@city_name and Month==@month_name and Product ==@product_name')

aa = df_select.groupby('Product') ['Total'].sum().sort_values()
fig_sp = px.bar(
    aa,
    x = aa.values,
    y = aa.index,
    title = "Sales by Product"
    )

a , b , c = st.columns(3)
a.plotly_chart(fig_sp, use_container_width = True)

fig_city = px.pie(
    df_select,
    values = 'Total',
    names = 'City',
    title = "Sales by City"
)

b.plotly_chart(fig_city, use_container_width = True)

bb = df_select.groupby('Month') ['Total'].sum().sort_values()
fig_month = px.bar(
    bb,
    x = bb.values,
    y = bb.index,
    title = "Sales by Product"
    )

c.plotly_chart(fig_month, use_container_width = True)

d , e = st.columns(2)


line_fig = px.line(
    bb,
    x = bb.values,
    y = bb.index,
    title = 'Sales by Month'
)

d.plotly_chart(line_fig, use_container_width = True)

scat_fig = px.scatter(
    df_select,
    x = 'Total',
    y = 'QuantityOrdered',
    title = 'Sales by Quantity'
)

e.plotly_chart(scat_fig, use_container_width = True)





    