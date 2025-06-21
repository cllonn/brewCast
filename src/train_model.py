import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("../data/coffee_shop_sales_dataset.csv")  # Adjust path if needed

# Drop unused or redundant columns if any
# Example: df.drop(['unnecessary_column'], axis=1, inplace=True)

# Convert categorical features (e.g., 'weekend') to numeric if needed
if df['weekend'].dtype == 'object':
    df['weekend'] = df['weekend'].map({'yes': 1, 'no': 0})

# Define feature set and label
features = ['average_temperature', 'humidity', 'rain', 'weekend', 'number_of_customers', 'coffee_ordered']
target = 'successful_day'  # This column must exist and be 0 or 1

X = df[features]
y = df[target]

# Handle missing values
X.fillna(X.mean(), inplace=True)

# Feature scaling (optional for Random Forest but useful for future model testing)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Optional: Feature importance
import matplotlib.pyplot as plt

importances = model.feature_importances_
plt.figure(figsize=(8, 5))
plt.barh(features, importances)
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.tight_layout()
plt.show()
