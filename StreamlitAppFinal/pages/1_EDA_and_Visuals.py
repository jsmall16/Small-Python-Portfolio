# --- Import necessary libraries ---
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load and parse dataset ---
coffee_data = pd.read_csv('Data/Cleaned_Data.csv', parse_dates=['transaction_date'])
coffee_data['transaction_time'] = pd.to_datetime(coffee_data['transaction_time'], format='%H:%M:%S').dt.time

# --- Feature engineering: Add readable month and clean text columns ---
coffee_data['month'] = coffee_data['transaction_date'].dt.strftime('%B %Y')

for col in ['store_location', 'product_category', 'product_type', 'product_detail']:
    coffee_data[col] = coffee_data[col].str.title().str.strip()

# --- Color palette for charts ---
coffee_palette = ['#A67B5B', '#C19A6B', '#8B6C42', '#D2B48C', '#6F4E37']

# --- Page title and filter controls ---
st.title("Explore the Data")
st.write("Use the filters below to explore sales performance by category, time, and location.")

# --- Filter widgets (Month, Location, Category) ---
col1, col2, col3 = st.columns(3)

with col1:
    selected_month = st.selectbox(
        "📅 Select Month:",
        sorted(coffee_data['month'].unique()),
        index=0
    )

with col2:
    selected_locations = st.multiselect(
        "📍 Store Location(s):",
        options=coffee_data['store_location'].unique(),
        default=coffee_data['store_location'].unique()
    )

with col3:
    selected_categories = st.multiselect(
        "🧾 Product Category:",
        options=coffee_data['product_category'].unique(),
        default=coffee_data['product_category'].unique()
    )

# --- Apply filters to dataset ---
filtered_data = coffee_data[
    (coffee_data['month'] == selected_month) &
    (coffee_data['store_location'].isin(selected_locations)) &
    (coffee_data['product_category'].isin(selected_categories))
]

# --- KPI Summary ---
st.markdown("### Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("💵 Total Revenue", f"${filtered_data['revenue'].sum():,.0f}")
col2.metric("🧾 Transactions", f"{filtered_data['transaction_id'].nunique():,}")
col3.metric("📦 Total Items Sold", f"{filtered_data['transaction_qty'].sum():,}")

# --- Chart 1: Product Category Breakdown ---
st.markdown("###  Sales by Product Category")
st.write("This chart shows the total quantity sold by product category during the selected time period and locations.")

cat_qty = filtered_data.groupby('product_category')['transaction_qty'].sum().sort_values()
fig1, ax1 = plt.subplots()
sns.barplot(x=cat_qty.values, y=cat_qty.index, palette=coffee_palette, ax=ax1)
ax1.set_title("Sales by Product Category")
ax1.set_xlabel("Quantity Sold")
ax1.set_ylabel("Product Category")
st.pyplot(fig1)

# --- Chart 2: Hourly Sales Trends ---
st.markdown("### Sales by Hour of Day")
st.write("This line chart illustrates customer purchasing behavior by hour. It can help identify peak business hours.")

hourly = filtered_data.groupby('hour')['transaction_qty'].sum()
fig2, ax2 = plt.subplots()
sns.lineplot(x=hourly.index, y=hourly.values, color='#6F4E37', marker='o')
ax2.set_title("Sales by Hour of Day")
ax2.set_xlabel("Hour")
ax2.set_ylabel("Quantity Sold")
st.pyplot(fig2)

# --- Chart 3: Weekly Sales Patterns ---
st.markdown("### Sales by Day of Week")
st.write("This chart shows total quantity sold across each day of the week, helping spot strong weekday or weekend performance.")

dow = filtered_data.groupby('day_of_week')['transaction_qty'].sum().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])
fig3, ax3 = plt.subplots()
sns.barplot(x=dow.index, y=dow.values, palette=coffee_palette, ax=ax3)
ax3.set_title("Sales by Day of Week")
ax3.set_xlabel("Day")
ax3.set_ylabel("Quantity Sold")
st.pyplot(fig3)

# --- Chart 4: Top Coffee Product Types ---
st.markdown("### Top 5 Coffee Product Types by Quantity (Filtered)")
st.write("This chart highlights the five most popular coffee product types, based on quantity sold for the selected filters.")

filtered_coffee = filtered_data[filtered_data['product_category'] == 'Coffee']
top_coffee_types = (
    filtered_coffee.groupby('product_type')['transaction_qty']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

fig_coffee, ax_coffee = plt.subplots()
sns.barplot(x=top_coffee_types.values, y=top_coffee_types.index, palette=['#6F4E37'] * 5, ax=ax_coffee)
ax_coffee.set_title("Top 5 Coffee Product Types (Filtered)")
ax_coffee.set_xlabel("Quantity Sold")
ax_coffee.set_ylabel("Product Type")
st.pyplot(fig_coffee)

# --- Chart 5: Revenue by Store Location ---
st.markdown("### Revenue by Store Location (Filtered)")
st.write("This bar chart shows which store locations drove the most revenue, based on the selected time period and product categories.")

revenue_by_location = (
    filtered_data.groupby('store_location')['revenue']
    .sum()
    .sort_values(ascending=False)
)

fig_loc, ax_loc = plt.subplots()
sns.barplot(x=revenue_by_location.index, y=revenue_by_location.values,
            palette=['#A67B5B', '#C19A6B', '#8B6C42'], ax=ax_loc)
ax_loc.set_title("Total Revenue by Store Location (Filtered)")
ax_loc.set_xlabel("Store Location")
ax_loc.set_ylabel("Revenue")
st.pyplot(fig_loc)
