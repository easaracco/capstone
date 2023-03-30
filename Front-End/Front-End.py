import pandas as pd
import requests
import streamlit as st
import altair as alt
from streamlit_option_menu import option_menu
from PIL import Image

# Fetch data from API
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data["result"])
    else:
        st.error(f"Error fetching data from {url}: {response.status_code}")
        return pd.DataFrame()

def plot_revenue_per_day_histogram(df):
    # Add a column with day numbers
    day_order = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    df['day_number'] = df['date'].map(day_order)

    # Generate the bar chart
    chart_perday = alt.Chart(df).mark_bar().encode(
        alt.X('date:N', title='Day of Week', sort=alt.EncodingSortField(field='day_number', order='ascending')),
        alt.Y('revenue:Q', title='Total Revenue'),
        tooltip=['date', 'revenue']
    ).properties(
        title='Total Revenue per Day'
    ).transform_calculate(
        day_number='datum.day_number'
    )

    return chart_perday

def plot_revenue_per_age_histogram(df):
    # Generate the bar chart
    chart_perage = alt.Chart(df).mark_bar().encode(
        alt.X('age:N', title='Age'),
        alt.Y('revenue:Q', title='Total Revenue'),
        tooltip=['age', 'revenue']
    ).properties(
        title='Total Revenue per Age'
    )

    return chart_perage


def plot_revenue_per_product_group_histogram(df):
    # Sort DataFrame by revenue in descending order
    df = df.sort_values('revenue', ascending=False)

    # Generate the bar chart
    chart = alt.Chart(df).mark_bar().encode(
        alt.X('product_group_name:N', title='Product Group', sort='-y'),
        alt.Y('revenue:Q', title='Total Revenue'),
        tooltip=['product_group_name', 'revenue']
    ).properties(
        title='Total Revenue per Product Group'
    )

    return chart


# Load data into DataFrames
articles_url = "https://api-dot-plucky-pointer-375715.ue.r.appspot.com/api/v1/articles"
customers_url = "https://api-dot-plucky-pointer-375715.ue.r.appspot.com/api/v1/customers"
transactions_url = "https://api-dot-plucky-pointer-375715.ue.r.appspot.com/api/v1/transactions"
KPI_url = "https://api-dot-plucky-pointer-375715.ue.r.appspot.com/api/v1/KPI"
KPI_age_url = "https://api-dot-plucky-pointer-375715.ue.r.appspot.com/api/v1/KPI_age"
KPI_date_url = "https://api-dot-plucky-pointer-375715.ue.r.appspot.com/api/v1/KPI_date"
KPI_product_group_url = "https://api-dot-plucky-pointer-375715.ue.r.appspot.com/api/v1/KPI_product_group"
KPI_saleschannel_url = "https://api-dot-plucky-pointer-375715.ue.r.appspot.com/api/v1/KPI_saleschannel"


articles_df = fetch_data(articles_url)
customers_df = fetch_data(customers_url)
transactions_df = fetch_data(transactions_url)
KPI_df = fetch_data(KPI_url)
KPI_age_df = fetch_data(KPI_age_url)
KPI_date_df = fetch_data(KPI_date_url)
KPI_product_group_df = fetch_data(KPI_product_group_url)
KPI_saleschannel_df = fetch_data(KPI_saleschannel_url)

articles_df=articles_df.drop('index', axis=1)
customers_df=customers_df.drop('index', axis=1)
transactions_df=transactions_df.drop('index', axis=1)
KPI_df=KPI_df.drop('index', axis=1)
KPI_age_df=KPI_age_df.drop('index', axis=1)
KPI_date_df=KPI_date_df.drop('index', axis=1)
KPI_product_group_df=KPI_product_group_df.drop('index', axis=1)
KPI_saleschannel_df=KPI_saleschannel_df.drop('index', axis=1)
daysordered=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Process date column
transactions_df['date'] = pd.to_datetime(transactions_df['date']).dt.date
KPI_df['date'] = pd.to_datetime(KPI_df['date']).dt.date
KPI_age_df['age']=KPI_age_df['age'].astype(int)
KPI_df['age']=KPI_df['age'].astype(int)
total_revenue = KPI_date_df['revenue'].sum()
total_customers = customers_df['customer_id'].nunique()
total_transactions = len(transactions_df)
KPI_saleschannel_df["percentage"] = KPI_saleschannel_df["revenue"] / KPI_saleschannel_df["revenue"].sum() * 100

Image=Image.open('hmlogo.png')

st.sidebar.image(Image, output_format='PNG', use_column_width=True)

with st.sidebar:
    page = option_menu(
        menu_title=None,
        options =['Home', 'KPI', 'Articles', 'Customers', 'Transactions']
    )

# Home
if page == 'Home':
    st.title('H&M Dashboard')
    st.subheader('Welcome to H&M Dashboard.')
    st.write('This dashboard is created to help H&M to understand their customers better and to help them to make better decisions.')
    st.write('1. KPI: This page shows the main table used to calculate the KPIs and 5 different charts disect revenue into different subgroups.')
    st.write('2. Articles: This page shows the full table of articles from H&M database.')
    st.write('3. Customers: This page shows the full table of customers from H&M database.')
    st.write('4. Transactions: This page shows the full table of transactions from H&M database.')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Revenue", value=f"{total_revenue:,.0f} €")
    with col2:
        st.metric(label="Total Customers", value=f"{total_customers}")
    with col3:
        st.metric(label="Total Transactions", value=f"{total_transactions}")

# KPI
elif page == 'KPI':
    st.title('KPI')

    #defining slider for sales channel
    saleschannel_lst = KPI_saleschannel_df["sales_channel_id"].to_list()
    filter_saleschannel = st.sidebar.multiselect(
        label='Sales Channel',
        options=saleschannel_lst,
        default= saleschannel_lst,
        key='saleschannel')

    #defining slider for product group
    productgroup_lst = KPI_product_group_df["product_group_name"].to_list()
    filter_productgroup = st.sidebar.multiselect(
        label='Product Group',
        options=productgroup_lst,
        default= productgroup_lst,
        key='productgroup')

    #defining slider for age
    age_min=KPI_age_df["age"].min()
    age_max=KPI_age_df["age"].max()
    filter_age = st.sidebar.slider(
        label='Age',
        min_value=int(age_min),
        max_value=int(age_max),
        value=(int(age_min), int(age_max)),
        key='age'
    )

    #defining slider for day
    days_lst = KPI_date_df["date"].to_list()
    filter_date = st.sidebar.multiselect(
        label='days',
        options=days_lst,
        default= daysordered,
        key='days')

    filter_age_df=KPI_age_df[(KPI_age_df["age"]>=filter_age[0]) & (KPI_age_df["age"]<=filter_age[1])]
    filter_date_df=KPI_date_df[KPI_date_df["date"].isin(filter_date)]
    filter_productgroup_df=KPI_product_group_df[KPI_product_group_df["product_group_name"].isin(filter_productgroup)]
    filter_saleschannel_df=KPI_saleschannel_df[KPI_saleschannel_df["sales_channel_id"].isin(filter_saleschannel)]

    # Show the table
    st.subheader('KPI Table')
    st.write(KPI_df)

    # Show the charts
    st.subheader('KPI Charts')

    revenue_per_day_histogram = plot_revenue_per_day_histogram(filter_date_df)
    st.altair_chart(revenue_per_day_histogram, use_container_width=True)

    revenue_per_age_histogram = plot_revenue_per_age_histogram(filter_age_df)
    st.altair_chart(revenue_per_age_histogram, use_container_width=True)

    revenue_per_product_group_histogram = plot_revenue_per_product_group_histogram(filter_productgroup_df)
    st.altair_chart(revenue_per_product_group_histogram, use_container_width=True)

    st.table(filter_saleschannel_df[['sales_channel_id', 'percentage']])

# Articles
elif page == 'Articles':
    st.title('Articles')

    # Show the table
    st.subheader('Articles Table')
    st.write(articles_df)

# Customers
elif page == 'Customers':
    st.title('Customers')


    # Show the table
    st.subheader('Customers Table')
    st.write(customers_df)

# Transactions
elif page == 'Transactions':
    st.title('Transactions')

    # Show the table
    st.subheader('Transactions Table')
    st.write(transactions_df)   




