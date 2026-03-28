import pandas as pd
import joblib
import os
import numpy as np

MODEL_PATH = 'models/best_model.pkl'
SCALER_PATH = 'models/scaler.pkl'
FEATURES_PATH = 'models/feature_names.pkl'

def make_prediction(input_data=None, *args, **kwargs):
    """
    The **kwargs here is a 'shield' that prevents the 4-argument TypeError.
    """
    # If for some reason input_data is empty but kwargs has data
    if input_data is None and kwargs:
        input_data = kwargs

    if not os.path.exists(MODEL_PATH): 
        return 0.0
    
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    feature_names = joblib.load(FEATURES_PATH)
    
    # Force into DataFrame and reorder
    input_df = pd.DataFrame([input_data])[feature_names]
    
    scaled_input = scaler.transform(input_df)
    score = model.predict(scaled_input)[0]
    
    # Logic Overrides
    if input_data.get('study_hours_per_day', 0) == 0:
        score = 0.0
        
    return round(float(np.clip(score, 0, 100)), 2)

def get_study_goal(current_input, target=90):
    temp_input = current_input.copy()
    for hours in np.arange(0.5, 15.5, 0.5):
        temp_input['study_hours_per_day'] = hours
        if make_prediction(temp_input) >= target:
            return float(hours)
    return None