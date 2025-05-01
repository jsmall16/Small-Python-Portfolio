# Import necessary libraries 
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Import Cofee Dataset 
coffee_data = pd.read_csv('Data/coffee-shop-sales-revenue.csv')

# Opening headers and text
st.title('Welcome to City Sips!☕️')
st.image('Images/Coffeeshop.jpg')
st.subheader('Where Data Meets Your Daily Brew📊')
st.write("""Welcome to **City Sips**, your go-to tool for brewing smarter business decisions and 
         exploring how New York drinks its coffee. Whether you're a coffee shop executive or just 
         curious how SoHo sips differently than Harlem, you're in the right place!
         """)
st.subheader(" What's Brewing Inside the App:")
st.write("""
         This app will allow business owners or coffee enthusiasts alike to:
         - Optimize product offerings and boost sales by exploring sales trends, top products, and customer behavior
         - Discover fun patterns in coffee trends across New York City
         - Use time series forecasting models to predict future sales and make strategic decisions
        """)

col1, col2 = st.columns([1, 1]) 

with col1:
    st.image("Images/NYC_map.jpg", use_column_width=True)  # Setting image path and size
    
with col2:
    st.markdown("""
    ### Coffee Trends Across NYC Neighborhoods

    This dataset includes over 140,000 coffee shop transactions from multiple store locations across Manhattan.

    Each transaction is tagged with:
    - 🗺️ A **neighborhood** like SoHo, Midtown, or the Upper West Side  
    - 📅 A **date and time** of purchase  
    - 🧾 A **product category**, type, and unit price  
    - 🔢 The **quantity sold** and store-level revenue

    By analyzing this data, we can uncover which neighborhoods prefer what drinks, when they buy them, and how that affects overall sales performance.
    """)