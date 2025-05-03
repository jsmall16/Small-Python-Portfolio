# --- Import necessary libraries ---
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# --- Homepage Title and Hero Image ---
st.title('☕️ Welcome to City Sips! ☕️')
st.image('Images/Coffeeshop.jpg')
st.subheader('Where Data Meets Your Daily Brew 📊')

# --- Intro Paragraph ---
st.write("""
City Sips is your go-to tool for brewing smarter business decisions and 
exploring how New Yorkers enjoy their coffee. Whether you're a coffee shop executive or 
just curious how Lower Manhattan differs from Astoria, you're in the right place!
""")
# --- App Purpose Summary ---
st.subheader("What's Brewing Inside the App 📲")
st.write("""
This app is designed to help business owners and coffee lovers alike:
- Optimize product offerings and boost sales through sales trends and product insights  
- Discover fun purchasing patterns across different store locations  
- Use forecasting models to predict future sales and plan more strategically
""")

# --- Section: NYC Map & Dataset Description ---
st.markdown("""### Coffee Trends from the Ground Up 🌱""")
st.write("""This dataset includes over **140,000 transactions** from **three unique store locations** across New York City:  
    **Lower Manhattan**, **Hell’s Kitchen**, and **Astoria**.""")
st.image("Images/Beans.jpeg")
st.markdown("""
    Each transaction is tagged with:
    - 📍 A **store location**  
    - 📅 A **date and time** of purchase  
    - 🧾 A **product category**, type, and unit price  
    - 🛍️ The **quantity sold** and store-level revenue

    By analyzing this data, we can uncover what customers are drinking, when they’re buying it, 
    and how each store’s performance compares.
    """)
st.markdown("### Use the sidebar on the left to navigate to **EDA & Visuals**!")
