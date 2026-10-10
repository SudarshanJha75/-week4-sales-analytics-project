
import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load dataset
df = pd.read_csv("data/sales_data.csv")
df.columns = df.columns.str.strip()

# 2. Prepare the data
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce"
)

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
df["total_price"] = pd.to_numeric(df["total_price"], errors="coerce")

# Extract date features
df["order_month"] = df["order_date"].dt.month
df["order_day"] = df["order_date"].dt.day
df["order_weekday"] = df["order_date"].dt.dayofweek

# Select features and target
features = [
    "quantity",
    "unit_price",
    "category",
    "sub_category",
    "product_name",
    "region",
    "order_month",
    "order_day",
    "order_weekday"
]

target = "total_price"

# Remove rows with missing required values
df = df.dropna(subset=features + [target]).copy()

X = df[features]
y = df[target]

# 3. Separate numeric and categorical columns
numeric_features = [
    "quantity", "unit_price",
    "order_month", "order_day", "order_weekday"
]

categorical_features = [
    "category", "sub_category", "product_name", "region"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", "passthrough", numeric_features),
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)

# 4. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# 5. Build the regression model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ))
])

# 6. Train the model
model.fit(X_train, y_train)

# 7. Make predictions
predictions = model.predict(X_test)

# 8. Evaluate model performance
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\nSALES PREDICTION MODEL RESULTS")
print("-" * 40)
print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")
print(f"MAE:  {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R-squared: {r2:.4f}")

# 9. Save results
os.makedirs("outputs", exist_ok=True)

results = pd.DataFrame({
    "Actual_Sales": y_test.to_numpy(),
    "Predicted_Sales": predictions,
    "Prediction_Error": y_test.to_numpy() - predictions
})

results.to_csv(
    "outputs/sales_predictions.csv", index=False
)

# Save the trained model
joblib.dump(model, "outputs/sales_model.pkl")

# Save evaluation metrics
metrics = pd.DataFrame({
    "Metric": ["MAE", "RMSE", "R2"],
    "Value": [mae, rmse, r2]
})

metrics.to_csv(
    "outputs/model_metrics.csv", index=False
)

print("\nModel trained successfully!")
print("Saved sales_predictions.csv")
print("Saved model_metrics.csv")
print("Saved sales_model.pkl")
