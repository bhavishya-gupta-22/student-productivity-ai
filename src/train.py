import os
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

def train_models():
    print("--- Training Models on New Dataset ---")
    
    # Load processed data
    X_train = pd.read_csv('data/X_train.csv')
    X_test = pd.read_csv('data/X_test.csv')
    y_train = pd.read_csv('data/y_train.csv').values.ravel()
    y_test = pd.read_csv('data/y_test.csv').values.ravel()
    
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
    }
    
    best_model = None
    best_r2 = -float('inf')
    best_name = ""
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        r2 = r2_score(y_test, preds)
        mae = mean_absolute_error(y_test, preds)
        
        print(f"[{name}] R2: {r2:.4f} | MAE: {mae:.2f}")
        
        if r2 > best_r2:
            best_r2 = r2
            best_model = model
            best_name = name

    # Save the absolute best
    print(f"\n🏆 Winner: {best_name}")
    joblib.dump(best_model, 'models/best_model.pkl')
    print("Model saved to models/best_model.pkl")

if __name__ == "__main__":
    train_models()