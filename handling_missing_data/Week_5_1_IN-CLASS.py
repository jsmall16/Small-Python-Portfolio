import pandas as pd            # Library for data manipulation
import seaborn as sns          # Library for statistical plotting
import matplotlib.pyplot as plt  # For creating custom plots
import streamlit as st         # Framework for building interactive web apps

# ================================================================================
#Missing Data & Data Quality Checks
#
# This lecture covers:
# - Data Validation: Checking data types, missing values, and ensuring consistency.
# - Missing Data Handling: Options to drop or impute missing data.
# - Visualization: Using heatmaps and histograms to explore data distribution.
# ================================================================================
st.title("Missing Data & Data Quality Checks")
st.markdown("""
This lecture covers:
- **Data Validation:** Checking data types, missing values, and basic consistency.
- **Missing Data Handling:** Options to drop or impute missing data.
- **Visualization:** Using heatmaps and histograms to understand data distribution.
""")

# ------------------------------------------------------------------------------
# Load the Dataset
# ------------------------------------------------------------------------------
# Read the Titanic dataset from a CSV file.
df = pd.read_csv("titanic.csv")

# ------------------------------------------------------------------------------
# Display Summary Statistics
# ------------------------------------------------------------------------------
# Show key statistical measures like mean, standard deviation, etc.
st.write("**Summary Statistics**")
st.write(df.shape)
st.dataframe(df.describe()) # only grabs numeric columns 
# use shape and describe to get summary stats

# ------------------------------------------------------------------------------
# Check for Missing Values
# Age is missing many values -- children? 
# ------------------------------------------------------------------------------
# Display the count of missing values for each column.
st.write("**Number of Missing Values by Column**")
st.dataframe(df.isnull().sum())
# mask of this value null, putting it over the entire df, and where there's null values
# you get true, otherwise false (true = 1, false = 0)

# ------------------------------------------------------------------------------
# Visualize Missing Data
# ------------------------------------------------------------------------------
# Create a heatmap to visually indicate where missing values occur.

st.subheader("Heatmap of missing values")
fig, ax = plt.subplots() #taking a blank canvas and putting it in python environment; giving python a blank canvas to draw the viz onto
sns.heatmap(df.isnull(), cmap = "viridis", cbar = False) #need extra code with streamlit; drawing the viz
st.pyplot(fig) # showing the viz
# ================================================================================
# Interactive Missing Data Handling
#
# Users can select a numeric column and choose a method to address missing values.
# Options include:
# - Keeping the data unchanged
# - Dropping rows with missing values
# - Dropping columns if more than 50% of the values are missing
# - Imputing missing values with mean, median, or zero
# ================================================================================

st.subheader("Handle Missing Data")
# Give audience ability to select a certain column to work with 
column = st.selectbox("Choose a column to fill", 
             df.select_dtypes(include=["number"]).columns)
# creates a list of column names where the column names are numeric data tpyes
# have to assign to a variable so that we can do something with it later; assigns the 
# string to the column variable name 

method = st.radio("Choose a method",
                  ["Original DF", "Drop Rows",
                   "Impute Mean","Impute Median","Impute Zero"]) 
# show all of your options at once; select different methods to employ

# Work on a copy of the DataFrame so the original data remains unchanged.
# df is going to stay untouched 
# df_clean is going to be a copy of df that will change with the custom filters 

df_clean = df.copy() # how we copy a data frame in pandas 
# if you only use the variable assignment, it will actually change df 

if method == "Original DF":
    pass # no transformation happening 
elif method == "Drop Rows":
    df_clean = df_clean.dropna(subset=[column]) # I want to select that column as the condition for dropping that row 
elif method == "Impute Mean":
    df_clean[column] = df_clean[column].fillna(df_clean[column].mean())
elif method == "Impute Median":
    df_clean[column] = df_clean[column].fillna(df_clean[column].median())
elif method == "Impute Zero":
    df_clean[column] = df_clean[column].fillna(0)
    


# Apply the selected method to handle missing data.

st.write(df_clean.describe())
st.dataframe(df_clean)

# ------------------------------------------------------------------------------
# Compare Data Distributions: Original vs. Cleaned
#
# Display side-by-side histograms and statistical summaries for the selected column.
# ------------------------------------------------------------------------------

st.subheader("Cleaned Data Distribution")

# How we make visualizations in streamlit 
fig,ax = plt.subplots() # This line puts in a blank canvas
sns.histplot(df_clean[column], kde = True) # drawing on the canvas
st.pyplot(fig) # showing (revealing) the canvas
# ZERO IS NOT A NEUTRAL NUMBER
# imputing mean, median, and zero heavily affect the data
col1, col2 = st.columns(2)

# --- Original Data Visualization ---
with col1:
    st.subheader("Original Data Distribution")
    # Plot a histogram (with a KDE) for the selected column from the original DataFrame.
    fig, ax = plt.subplots()
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(f"Original Distribution of {column}")
    st.pyplot(fig)
    st.subheader(f"{column}'s Original Stats")
    # Display statistical summary for the selected column.
    st.write(df[column].describe())

# --- Cleaned Data Visualization ---
with col2:
    st.subheader("Cleaned Data Distribution")
    # Plot a histogram (with a KDE) for the selected column from the cleaned DataFrame.
    fig, ax = plt.subplots()
    sns.histplot(df_clean[column], kde=True)
    plt.title(f"Distribution of {column} after {method}")
    st.pyplot(fig)
    st.subheader(f"{column}'s New Stats")
    # Display statistical summary for the cleaned data.
    st.write(df_clean[column].describe())