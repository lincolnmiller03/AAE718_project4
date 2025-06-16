from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

def train_model(df):
    # Clean the data
    df = df[df["median_income"] > 0].dropna()

    # Features and target
    X = df.drop(columns=["median_income", "state", "county"])
    y = np.log(df["median_income"])  # log-transform target

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    print("Train R^2 Score:", r2_score(y_train, y_pred_train))
    print("Test R^2 Score:", r2_score(y_test, y_pred_test))

    # Plot predicted vs actual (in original scale)
    plt.scatter(np.exp(y_test), np.exp(y_pred_test), alpha=0.5)
    plt.xlabel("Actual Median Income")
    plt.ylabel("Predicted Median Income")
    plt.title("Actual vs Predicted Median Income")
    plt.grid(True)
    plt.savefig('project4.png')
    plt.show()

    return model