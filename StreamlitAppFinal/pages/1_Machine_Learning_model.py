# Importing necessary libraries for data manipulation and visualization 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
# Libraries for regression 
from sklearn.model_selection import train_test_split # for splitting the data 
from sklearn.linear_model import LinearRegression # for modeling
from sklearn.metrics import mean_squared_error, r2_score # for evaluating model performance 


# Load the dataset
coffee_data = pd.read_csv('StreamlitAppFinal/Data/coffee-shop-data.csv')

# Data cleaning 
# Ensures unit price and quantity are numeric data types. If not, sets them as NaN
coffee_data['unit_price'] = pd.to_numeric(coffee_data['unit_price'], errors='coerce')
coffee_data['transaction_qty'] = pd.to_numeric(coffee_data['transaction_qty'], errors='coerce')
# Creates a new column to calculate the total sale amount for each transaction
coffee_data['total_sales'] = coffee_data['unit_price'] * coffee_data['transaction_qty']

# Drop rows with missing values
coffee_data.dropna(subset=['unit_price', 'transaction_qty', 'store_location', 'product_category', 'day_of_week', 'hour'], inplace=True)

# Keep numeric features separate
numeric_features = coffee_data[['unit_price', 'hour', 'transaction_qty']]

# Converting categorical variables into dummy variables 
categorical_features = pd.get_dummies(
    coffee_data[['store_location', 'product_category', 'day_of_week']],
    drop_first=True
)

# Combine them into one variable that contains all the predictors 
coffee_data_encoded = pd.concat([numeric_features, categorical_features], axis=1)

# Define features and target
X = coffee_data_encoded # independent variables (different predictors you are testing)
y = coffee_data['total_sales'] # dependent variable (target variable)

# Split the data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, 
                                                    random_state=42)

# Train the linear regression on the training data 
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions using the testing data
y_pred = model.predict(X_test)

# Evaluate model performance (mean squared error and r squared)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Preparing the streamlit app
# Create streamlit title
st.title("Predicting Coffee Shop Sales 📈")

st.markdown("""
The most important thing for any business owner is to forecast when they will have the most sales, 
in order to ensure that they have the necessary staffing and supply to keep up with it. Knowing these trends can be
critical to improving the customer experience. Using a linear regression model, this dashboard predicts total sales based on:
- Unit Price
- Hour of Day
- Store Location
- Product Category
- Day of Week
""")

# Creating a scatterplot to compare the actual testing data vs. the predictions 
st.markdown("### Actual vs. Predicted Sales")
fig, ax = plt.subplots()
sns.scatterplot(x=y_test, y=y_pred, alpha=0.5, color="#6F4E37", edgecolor="w")
ax.set_xlabel("Actual Total Sales")
ax.set_ylabel("Predicted Total Sales")
ax.set_title("Actual vs. Predicted Total Sales")
st.pyplot(fig)

st.markdown(f"""
As we can see, the model we deployed for this data performed well, explaining around **{r2:.2%}** of the variance in sales. Therefore, it serves as a useful modeling for forecasting when these coffee shops will be the most successful. 
""")

# Extracts the coefficients and sorts them in order of importance (influence) on the predictive model
coefficients = pd.Series(model.coef_, index=X.columns).sort_values()

st.markdown("### Most Influential Predictors")
st.write("""These graphs display the most influential predictors that lead to an increase or 
            decrease in sales.
         """)

# Top 10 Positive Predictors that increase total sales
fig_imp, ax_imp = plt.subplots(figsize=(8, 6))
coefficients.tail(10).plot(kind='barh', color='#6F4E37', ax=ax_imp)
ax_imp.set_title("Top 10 Positive Predictors")
st.pyplot(fig_imp)

# Top 10 Negative Predictors that decrease total sales
fig_imp2, ax_imp2 = plt.subplots(figsize=(8, 6))
coefficients.head(10).plot(kind='barh', color='gray', ax=ax_imp2)
ax_imp2.set_title("Top 10 Negative Predictors")
st.pyplot(fig_imp2)

st.markdown("### So What’s Brewing in Sales Trends? ☕")

st.write("""
        Higher-priced drinks like Drinking Chocolate, Signature Teas, and Specialty Coffees are the best-performing items that 
        ultimately drive the most sales. Saturdays in Lower Manhattan consistently see larger transactions, possibly due to the nature
        of the weekend or tourists.
        """)

st.write("""
         Meanwhile, Coffee Beans and Branded Merch tend to bring in smaller totals. There is also a bit of a midweek slump, with Tuesdays and Sundays
         trailing behind.
         """)

st.markdown("""### These patterns help business owners plan smarter by accurately deciding when to stock up, what to feature, and how to keeep sales flowing.
""")