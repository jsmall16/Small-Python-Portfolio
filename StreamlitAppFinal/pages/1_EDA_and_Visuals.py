# Import necessary libraries 
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# Import Cofee Dataset 
coffee_data = pd.read_csv('Data/coffee-shop-sales-revenue.csv', delimiter='|')

st.dataframe(coffee_data)