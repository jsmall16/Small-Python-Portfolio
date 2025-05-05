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

# Species and Island Filter 
st.markdown("### 🔍 Filter by Species and Island")
st.write("Filter by penguin species and their island habitat to explore more specific data slices.")

# Dropdowns for filtering
species_list = penguins["species"].dropna().unique()
island_list = penguins["island"].dropna().unique()

# Create two different columns to have the filters
col1, col2 = st.columns(2)
with col1:
    selected_species = st.selectbox("Choose a species:", species_list)
with col2:
    selected_island = st.selectbox("Choose an island:", island_list)

# Apply both filters
filtered_data = penguins[
    (penguins["species"] == selected_species) & 
    (penguins["island"] == selected_island)
]

# Display filtered data
st.markdown(f"#### Displaying data for `{selected_species}` penguins on `{selected_island}`")
st.dataframe(filtered_data)

# Summary Stats for filtered data
st.markdown("### Summary Statistics")
st.write(f"Let's explore summary statistics for the `{selected_species}` penguins on `{selected_island}`:")
st.write(filtered_data.describe())

# Visualization of body mass by species
st.markdown("### Count of Penguins by Species")
st.write("To get a better sense of the data, let's look at how many penguins there are of each species.")

# Create the count data
species_counts = penguins["species"].value_counts().reset_index()
species_counts.columns = ["species", "count"]

# Plotting
fig, ax = plt.subplots()
ax.bar(species_counts["species"], species_counts["count"], color="skyblue")
ax.set_ylabel("Count")
ax.set_xlabel("Species")
ax.set_title("Number of Penguins per Species")

st.pyplot(fig)

st.markdown("## Thanks for waddling through the data with us!")