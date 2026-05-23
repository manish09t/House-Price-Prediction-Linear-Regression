# Import the pandas library for data manipulation
import pandas as pd

# Read the data from a CSV file named "Multi.csv" into a pandas DataFrame
df = pd.read_csv("Multi.csv")

# Display the DataFrame to see the data
print("The full DataFrame:")
print(df)

# Define the features (independent variables) for the model
# The features are 'area', 'bedrooms', and 'age'
x = df[["area", "bedrooms", "age"]]

# Display the features DataFrame
print("\nFeatures (x):")
print(x)

# Define the target variable (dependent variable)
# The target is 'price'
y = df.price

# Display the target series
print("\nTarget (y):")
print(y)

# Import the LinearRegression model from scikit-learn
from sklearn.linear_model import LinearRegression

# Create an instance of the LinearRegression model
model = LinearRegression()

# Train the model using the features (x) and target (y)
model.fit(x, y)

# Print the coefficients of the model
# These represent the weights for each feature
print("\nModel coefficients:")
print(model.coef_)

# Print the y-intercept of the model
print("\nModel intercept:")
print(model.intercept_)

# Make a prediction for a new data point with area=5000, bedrooms=3, and age=5
# To avoid the UserWarning, we create a new DataFrame for the prediction
new_data = pd.DataFrame([[5000, 3, 5]], columns=["area", "bedrooms", "age"])
print("\nPrediction for a new data point:")
print(model.predict(new_data))