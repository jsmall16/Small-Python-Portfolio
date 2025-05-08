# Import necessary libraries
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Data Cleaning Steps:
# Load and parse dataset
coffee_data = pd.read_csv('StreamlitAppFinal/Data/coffee-shop-data.csv')

# Converting the date columns into datetime objects for easy aggregation
coffee_data['transaction_date'] = pd.to_datetime(coffee_data['transaction_date'])
# Converting the time column into a datetime object (formatted as hours,mins,sec) --> extracting only the time portion
coffee_data['transaction_time'] = pd.to_datetime(coffee_data['transaction_time'], format='%H:%M:%S').dt.time

# Extracting the month and year from the transaction_date column and creating a month column
coffee_data['month'] = coffee_data['transaction_date'].dt.strftime('%B %Y')

# This for loop looks at four columns in the dataset and standardizes the formatting across them
# Text is converted to title case and trailing white spaces are removed (to ensure consistency)
for col in ['store_location', 'product_category', 'product_type', 'product_detail']:
    coffee_data[col] = coffee_data[col].str.title().str.strip()

# Creating a custom color palette
coffee_palette = ['#A67B5B', '#C19A6B', '#8B6C42', '#D2B48C', '#6F4E37']

# Create a page introduction section
st.markdown("## Behind the Beans: NYC coffee insights")
st.write("Let's dive into what, where, and when New Yorkers are sipping. Use the filters below to explore sales performance by category, time, and location.")

### filtering section 

# Creating columns to divide the page into 3 different sections
col1, col2, col3 = st.columns(3)

# Sorts the month column into the unique months, starting with the first month in the sort
# A drop down menu is created from the sorted list where users select the Month they are looking for
with col1:
    selected_month = st.selectbox(
        "📅 Select Month:",
        sorted(coffee_data['month'].unique()),
        index=0
    )
# Gathering the unique store locations from the store_location column
# Users can select from one or multiple store locations (multiselect box)
# By default, all store locations are selected
with col2:
    selected_locations = st.multiselect(
        "📍 Store Location(s):",
        options=coffee_data['store_location'].unique(),
        default=coffee_data['store_location'].unique()
    )
# A multiselect box with unique product categories 
# By default, all categories are selected
with col3:
    selected_categories = st.multiselect(
        "🧾 Product Category:",
        options=coffee_data['product_category'].unique(),
        default=coffee_data['product_category'].unique()
    )

# Apply filters to dataset based on the users' selections
# Creates a filtered dataframe that reflects the filtering of the users' selections
filtered_data = coffee_data[
    (coffee_data['month'] == selected_month) &
    (coffee_data['store_location'].isin(selected_locations)) &
    (coffee_data['product_category'].isin(selected_categories))
]

# Title to introduce the next chart
st.markdown("###  Sales by Product Category")
st.write("This chart shows the total quantity sold by product category during the selected time period and locations.")

# Groups the filtered data by product_category
# Sums up the transaction_qty for each category
# Sorts the results in ascending order (so the bar chart will look cleaner)
cat_qty = filtered_data.groupby('product_category')['transaction_qty'].sum().sort_values()
fig1, ax1 = plt.subplots() 
sns.barplot(x=cat_qty.values, y=cat_qty.index, palette=coffee_palette, ax=ax1) # Using the color palette we previously created 
ax1.set_title("Sales by Product Category")
ax1.set_xlabel("Quantity Sold")
ax1.set_ylabel("Product Category")
st.pyplot(fig1)

# Title to introduce the next chart 
st.markdown("### Sales by Hour of Day")
st.write("This line chart illustrates customer purchasing behavior by hour. It can help identify peak business hours.")

# Groups the filtered data by hour 
# Sums up the transaction quantity for each hour
hourly = filtered_data.groupby('hour')['transaction_qty'].sum()
fig2, ax2 = plt.subplots() 
sns.lineplot(x=hourly.index, y=hourly.values, color='#6F4E37', marker='o')
ax2.set_title("Sales by Hour of Day")
ax2.set_xlabel("Hour")
ax2.set_ylabel("Quantity Sold")
st.pyplot(fig2)

# Title to introduce the next chart 
st.markdown("### Sales by Day of Week")
st.write("This chart shows total quantity sold across each day of the week, helping to identify strong daily performances.")


# Groups the filtered data by day_of_week
# Sums up the total transaction_qty for each day
# Using reindex() to ensure the days are in calendar order (not alphabetical)
dow = filtered_data.groupby('day_of_week')['transaction_qty'].sum().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])
fig3, ax3 = plt.subplots()  
sns.barplot(x=dow.index, y=dow.values, palette=coffee_palette, ax=ax3) # Using the color palette we previously created 
ax3.set_title("Sales by Day of Week")
ax3.set_xlabel("Day")
ax3.set_ylabel("Quantity Sold")
st.pyplot(fig3)

# Title to introduce the next chart 
st.markdown("### Top 5 Coffee Product Types by Quantity")
st.write("This chart highlights the five most popular coffee product types, based on quantity sold for the selected filters.")

# Filters the product category to only be coffee
filtered_coffee = filtered_data[filtered_data['product_category'] == 'Coffee']
top_coffee_types = (
    filtered_coffee.groupby('product_type')['transaction_qty'] # Groups the data by coffee type
    .sum() # Sums up the quantity sold for each coffee type
    .sort_values(ascending=False) # Sorts the result from most sold to least sold
    .head(5) # Takes only the top 5 best-selling coffee types
)

fig_coffee, ax_coffee = plt.subplots()
sns.barplot(x=top_coffee_types.values, y=top_coffee_types.index, palette=['#6F4E37'] * 5, ax=ax_coffee)
ax_coffee.set_title("Top 5 Coffee Product Types")
ax_coffee.set_xlabel("Quantity Sold")
ax_coffee.set_ylabel("Product Type")
st.pyplot(fig_coffee)

# Title to introduce the next chart 
st.markdown("### Revenue by Store Location")
st.write("This bar chart shows which store locations drove the most revenue, based on the selected time period and product categories.")

# Grouping the filtered data by store location 
revenue_by_location = (
    filtered_data.groupby('store_location')['revenue']
    .sum() # Sum up the revenue for each store location 
    .sort_values(ascending=False)
)

fig_loc, ax_loc = plt.subplots() 
sns.barplot(x=revenue_by_location.index, y=revenue_by_location.values,
            palette=['#A67B5B', '#C19A6B', '#8B6C42'], ax=ax_loc)
ax_loc.set_title("Total Revenue by Store Location")
ax_loc.set_xlabel("Store Location")
ax_loc.set_ylabel("Revenue")
st.pyplot(fig_loc)

# Used data-to-viz to assist with the constuction of these plots 