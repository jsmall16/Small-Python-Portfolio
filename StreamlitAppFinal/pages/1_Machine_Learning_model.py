# Import necessary libraries
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

coffee_data = pd.read_csv('Data/Cleaned_Data.csv')
coffee_data['unit_price'] = pd.to_numeric(coffee_data['unit_price'], errors='coerce')
coffee_data['transaction_qty'] = pd.to_numeric(coffee_data['transaction_qty'], errors='coerce')
coffee_data['total_sales'] = coffee_data['unit_price'] * coffee_data['transaction_qty']
coffee_data.dropna(subset=['unit_price', 'transaction_qty', 'store_location', 'product_category', 'day_of_week', 'hour'], inplace=True)

# --- One-hot encode categorical variables ---
data_encoded = pd.get_dummies(coffee_data[['unit_price', 'hour', 'store_location', 'product_category', 'day_of_week']], drop_first=True)
X = data_encoded
y = coffee_data['total_sales']

# --- Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Train the linear regression model ---
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# --- Model evaluation ---
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# --- Streamlit App Layout ---
st.title("Predicting Coffee Shop Sales 📈")

st.markdown("""
Using a **linear regression model**, this dashboard predicts total sales based on:
- Unit Price
- Hour of Day
- Store Location
- Product Category
- Day of Week
""")

# --- Visualize actual vs predicted ---
st.markdown("### Actual vs. Predicted Sales")
fig, ax = plt.subplots()
sns.scatterplot(x=y_test, y=y_pred, alpha=0.5, color="#6F4E37", edgecolor="w")
ax.set_xlabel("Actual Total Sales")
ax.set_ylabel("Predicted Total Sales")
ax.set_title("Actual vs. Predicted Total Sales")
st.pyplot(fig)

# --- Commentary ---
st.markdown("""
The model performs well overall, explaining around **71%** of the variance in sales. Some variance at extreme values
suggests future models could benefit from more granular features or nonlinear modeling techniques.
""")

# Get feature importance
coefficients = pd.Series(model.coef_, index=X.columns).sort_values()


# Plot top and bottom 10
st.markdown("### Most Influential Predictors")
fig_imp, ax_imp = plt.subplots(figsize=(8, 6))
coefficients.tail(10).plot(kind='barh', color='#6F4E37', ax=ax_imp)
ax_imp.set_title("Top 10 Positive Predictors")
st.pyplot(fig_imp)

fig_imp2, ax_imp2 = plt.subplots(figsize=(8, 6))
coefficients.head(10).plot(kind='barh', color='gray', ax=ax_imp2)
ax_imp2.set_title("Top 10 Negative Predictors")
st.pyplot(fig_imp2)

st.write("""Based on our linear regression model, the strongest drivers of total 
         sales include higher unit price items like Drinking Chocolate, Tea, and Coffee.
         Transactions in Lower Manhattan and on Saturdays also tend to be larger in value. 
         On the flip side, categories like Coffee Beans and Branded Merchandise are linked 
         to lower total sales, along with midweek purchases and Sunday traffic. These insights 
         help identify what products and time slots are most profitable — valuable input for 
         inventory planning and promotional strategies""")