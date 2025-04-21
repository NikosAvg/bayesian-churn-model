import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_telco_data(df):
    # Drop customerID
    df = df.drop(columns=['customerID'])

    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna(subset=['TotalCharges'])

    # Encode target
    df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})

    # Identify categorical and numerical columns
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

    # Encode categorical features
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    # Scale numeric features
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df