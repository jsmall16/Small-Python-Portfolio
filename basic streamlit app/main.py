# Make sure streamlit and pandas are installed
import streamlit as st
import pandas as pd 

# App title 
st.title('Penguins App')
st.subheader('Welcome to the Penguins app where  you can sort and filter through data about penguins in an easy and accessible way!')
# Description of what the app does 
st.image('Penguins.png') # Import image of penguins 

st.write("Here is the whole dataset!")
penguins = pd.read_csv("data/penguins.csv") # Load the dataset 
penguins_st = st.dataframe(penguins) # displaying the dataset on streamlit 

st.write("That's a lot of penguins to look at!")
st.write("Let's filter by species to get a better understanding of the dataset.")

# Dropdown to select the species 
penguins_select = st.selectbox('Select a species of penguin:', penguins["species"].unique())
st.write(f'Here are the {penguins_select} penguins:') # f string to match what the users select 
filtered_df = penguins[penguins['species'] == penguins_select] # creating the filter based on user selection
st.dataframe(filtered_df) # displaying the filtered dataframe 

st.write("Now our dataset is more manageable to look at!")

st.subheader("Look at a few different species to get a feel for the data. Enjoy!")