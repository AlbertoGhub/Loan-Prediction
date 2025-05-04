# SHOWING NaNs
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import cross_val_score
from collections import OrderedDict
from sklearn.model_selection import train_test_split

# DATA TYPE, AND NA CALCULATOR
def na_calculator(data):
    '''SHOWING THE STATS OF MISSING DATA AND DATA TYPE'''

    percentage_missing = np.around(data.isna().mean()*100, 2).sort_values(ascending = False)                      # Storing the Percentages of NaNs
    sum_missing = data.isna().sum().sort_values(ascending = False)                                    # Storing the Sum of NaNs
    names = sum_missing.index.to_list()                                                               # Storing names (to show in the columns)
    data_type = data[names].dtypes                                                                    # Storing the type of data based on the order from the previous obtained data (slicing)
    sum_values = sum_missing.to_list()                                                                # Getting count of missing values
    perc_values = np.around(percentage_missing.to_list(), 3)                                          # Getting percentage of missing values
    types = data_type.to_list()                                                                       # Getting the types of the data
    
    # TURN ALL THE DATA INTO A DATAFRAME
    df_missing = pd.DataFrame({"NAMES" : names,
                                    "VALUE COUNT" : sum_values,
                                    "PERCENTAGE (%)" : perc_values,
                                    "DATA TYPE": types})
    return df_missing

# FILLING MISSING DATA
def imputing_missing_data(df):
    
    """THIS FUNCTION WILL FILL THE NA BASED ON THE DATA TYPE
    
        1. IF IT IS STRING, WILL FILL WITH MODE
        2. OTHERWISE, WILL FILL WITH MEDIAN"""
    
    column_names = list(df.columns) # Getting the names so we can loop through
    
    for name in column_names:
        
        if(df[name].dtypes != "object" and df[name].isna().sum() > 0): # numbers, we apply median
            df[name].fillna(df[name].median(), inplace = True)            
        elif(df[name].dtypes == "object" and df[name].isna().sum() > 0): # Objects, we apply mode
            df[name].fillna(df[name].mode()[0], inplace = True)

# MODELLING AND TRAINING PHASE

def train_test_pred(X_train, y_train, X_test, y_test):
    """
    Trains and evaluates multiple classification models.
    
    Returns:
        1. DataFrame with performance metrics,
        2. Series with model rankings,
        3. The best model instance,
        4. The name of the best model.
    """
    
    models = {
        'Logistic Regression'  : LogisticRegression(max_iter=1000),
        'Random Forest'        : RandomForestClassifier(),
        'XGBoost Classifier'   : XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    }

    performance = {}

    for name, model in models.items():
        # Cross-validation (optional - can be removed if not needed)
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
        
        # Training
        model.fit(X_train, y_train)
        
        # Prediction
        y_pred = model.predict(X_test)

        # Evaluation metrics
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='binary')

        performance[name] = {
            'Accuracy' : f'{np.around(acc*100, 2)}%',
            'F1 Score' : f'{np.around(f1*100, 2)}%'
        }

    return pd.DataFrame(performance)
