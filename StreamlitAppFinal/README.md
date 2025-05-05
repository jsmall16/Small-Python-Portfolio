# ☕ City Sips: NYC Coffee Sales App ☕
![CoffeeShop](Images/Coffeeshop.jpg)

## Project Overview 
City Sips is an interactive Streamlit app that helps NYC coffee shop owners and enthusiasts alike to make smarter business decisions. This app will provide strategic insights into: 
- Which products generate the most revenue
- What locations have the most sales
- What time of day should inventory be the most stocked
- And more!

## Dataset Description
This app uses the Maven Roasters: Coffee Shop Sales & Revenue Data from [Kaggle](https://www.kaggle.com/datasets/agungpambudi/trends-product-coffee-shop-sales-revenue-dataset/code). This dataset contains: 
- Over 140,000 transactions collected from 3 different store locations:
    - **Lower Manhattan, Hell's Kitchen, & Astoria**
- Each transaction includes:
    - Store location
    - Date/time of purchase
    - Product category and unit price
    - Quantity sold and total revenue

This dataset is critical for providing stakeholders with strategic insights to understand product performance and user behavior.

## App Features 

### 1️⃣ **Sidebar Navigation**

The sidebar feature of this app allows you to toggle between different pages, exploring the Home Page, the EDA & Visuals Page, and the Machine Learning Model Page. 

<img src="Images/Sidebar.png" alt="Sidebar Navigation" width="600">

### 2️⃣ **Exploratory Data Analysis**

This section allows users to interact with the data more closely to gain more personalized insights. Users can filter by Month, Store location, or Product Category, to get the most out of their visualizations. 

<img src="Images/Filters.png" alt="Filters" width="600">

There are many different visuals in this app that change dyanmically with user selections. These relate to product category, time of day, day of week, and store location. 

<img src="Images/Bar-graph.png" alt="Graph" width="600">

### 3️⃣ Machine Learning Model 

The final page of this app utilizes a linear regression model with a ~70% explainability to assess the most and least influential predictors for coffee shop sales. The goal of implementing this model is to help the users identify what factors will forecast future sales, allowing them to stock and staff appropriately. 

<img src="Images/Predicted.png" alt="Predicted vs. actuals" width="600">

<img src="Images/Influential.png" alt="Predictors" width="600">


