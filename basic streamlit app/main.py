# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import title and subjeader
st.title("🐧 Penguins Explorer 🐧")
st.image("Penguins.png", use_column_width=True)
st.subheader("Dive into Penguin Data in a Simple and Interactive Way")

# App description and purpose
st.markdown("""
Welcome to the Penguins Explorer App! Use this tool to explore, sort, and filter data on different penguin species.
This dataset includes information on their physical characteristics and habitat locations.
""")

# Load Dataset
penguins = pd.read_csv("data/penguins.csv")

# Show Full Dataset
st.markdown("### Full Penguins Dataset")
st.dataframe(penguins)
st.write("Here is the full dataset comprising the different penguin attributes!")

# --- Species Filter 
st.markdown("### 🔍 Filter by Species")
st.write("Filter by different penguin species to explore individual penguin features!")
species_list = penguins["species"].dropna().unique()
selected_species = st.selectbox("Choose a species:", species_list)

filtered_data = penguins[penguins["species"] == selected_species]

st.markdown(f"#### Displaying data for: `{selected_species}`")
st.dataframe(filtered_data)

# Summary Stats
st.markdown("### Summary Statistics")
st.write("Let's explore some basic summary statistics!")
st.write(filtered_data.describe())

# Visualization 
st.write("In order to get a better sense of the data, let's visualize the body mass of the penguins by species!")
st.markdown("### 🧊 Average Body Mass by Species")
avg_mass = penguins.groupby("species")["body_mass_g"].mean().reset_index()

fig, ax = plt.subplots()
ax.bar(avg_mass["species"], avg_mass["body_mass_g"])
ax.set_ylabel("Average Body Mass (g)")
ax.set_xlabel("Species")
ax.set_title("Average Body Mass per Penguin Species")

st.pyplot(fig)

# Closing Message
st.markdown("---")
st.success("Happy exploring!")
 