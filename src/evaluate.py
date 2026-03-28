import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

def evaluate_complex_data():
    print("--- Generating Advanced Analytics ---")
    os.makedirs('outputs', exist_ok=True)
    
    # 1. Correlation Heatmap (Very important for 18 columns!)
    df = pd.read_csv('data/student_data.csv').drop(columns=['student_id', 'age'], errors='ignore')
    # Filter for only numeric columns for the heatmap
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    plt.figure(figsize=(14, 10))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='viridis', fmt=".2f")
    plt.title("Correlation Matrix of Student Habits")
    plt.savefig('outputs/full_correlation_matrix.png')
    plt.close()

    # 2. Feature Importance (Only works if Best Model is Tree-based)
    model = joblib.load('models/best_model.pkl')
    features = joblib.load('models/feature_names.pkl')
    
    if hasattr(model, 'feature_importances_'):
        importance_df = pd.DataFrame({
            'Feature': features,
            'Importance': model.feature_importances_
        }).sort_values(by='Importance', ascending=False)

        plt.figure(figsize=(10, 6))
        sns.barplot(x='Importance', y='Feature', data=importance_df, palette='magma')
        plt.title("What Drives Productivity Most?")
        plt.tight_layout()
        plt.savefig('outputs/feature_importance.png')
        print("Feature importance chart created.")
    
    print("All plots saved in /outputs/")

if __name__ == "__main__":
    evaluate_complex_data()