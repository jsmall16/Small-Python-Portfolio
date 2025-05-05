# Import necessary libraries
import streamlit as st

# Homepage Title & Image
st.title('Welcome to City Sips! ☕️')
st.image('StreamlitAppFinal/Images/Coffeeshop.jpg')
st.subheader('Where Data Meets Your Daily Brew 📊')

# Intro Paragraph
st.write("""
City Sips is your go-to tool for brewing smarter business decisions and 
exploring how New Yorkers enjoy their coffee. Whether you're a coffee shop executive or 
just curious how different New York neighborhoods enjoy their coffee, you're in the right place!
""")
# Purpose of App
st.subheader("What's Brewing Inside the App 📲")
st.write("""
This app is designed to help business owners and coffee lovers alike:
- Boost sales by analyzing product and sales trends  
- Use predictive models to forecast future sales
The goal is to help coffee shop owners make more strategic business decisions.
""")

# Dataset description
st.markdown("""### Coffee Trends from the Ground Up 🌱""")
st.write("""This dataset includes over 140,000 transactions from three unique coffee shop locations across New York City:  
    **Lower Manhattan**, **Hell’s Kitchen**, and **Astoria**.""")
st.markdown("""
    Each transaction contains:
    -  A store location
    -  A date/time of purchase  
    -  A product category, type, and unit price  
    -  The quantity sold and revenue

    By analyzing this data, we can uncover what customers are drinking, when they’re buying it, 
    and how each store’s performance compares. 
    """)
st.markdown("### Use the sidebar on the left to navigate to **EDA & Visuals**!")
