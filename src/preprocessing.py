import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess_data():
    print("--- Starting Advanced Preprocessing ---")
    data = pd.read_csv('data/student_data.csv')
    
    # 1. Drop columns that don't help prediction (ID, Age, Gender)
    # Keeping it simple for now, but we'll use everything else
    cols_to_drop = ['student_id', 'age', 'gender', 'productivity_score']
    X = data.drop(columns=cols_to_drop)
    y = data['productivity_score']
    
    # 2. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Scaling (CRITICAL for these new large numbers like coffee_intake)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 4. Save Scaler and Data
    os.makedirs('models', exist_ok=True)
    joblib.dump(scaler, 'models/scaler.pkl')
    
    # Store column names so predict.py knows the order
    joblib.dump(X.columns.tolist(), 'models/feature_names.pkl')
    
    pd.DataFrame(X_train_scaled, columns=X.columns).to_csv('data/X_train.csv', index=False)
    pd.DataFrame(X_test_scaled, columns=X.columns).to_csv('data/X_test.csv', index=False)
    y_train.to_csv('data/y_train.csv', index=False)
    y_test.to_csv('data/y_test.csv', index=False)
    
    print(f"Preprocessed with {len(X.columns)} features.")

if __name__ == "__main__":
    preprocess_data()