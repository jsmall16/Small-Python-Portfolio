
import streamlit as st
import pandas as pd 

st.title('Penguins App')
st.subheader('Welcome to the Penguins app where  you can sort and filter through data about penguins in an easy and accessible way!')
st.image('Penguins.png')

st.write("Here is the whole dataset!")
penguins = pd.read_csv("data/penguins.csv")
penguins_st = st.dataframe(penguins)

st.write("That's a lot of penguins to look at!")
st.write("Let's filter by species to get a better understanding of the dataset.")

penguins_select = st.selectbox('Select a species of penguin:', penguins["species"].unique())
st.write(f'Here are the {penguins_select} penguins:')
filtered_df = penguins[penguins['species'] == penguins_select]
st.dataframe(filtered_df)

st.write("Now our dataset is more manageable to look at!")

st.subheader("Enjoy!")