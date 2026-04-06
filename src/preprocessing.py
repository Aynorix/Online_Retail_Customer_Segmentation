import pandas as pd
import numpy as np

def run_preprocessing_pipeline(file_path):
    """
    Transforms raw retail data into a multi-feature RFM + Context table.
    """
    df = pd.read_csv(file_path)
    
    # 1. Cleaning
    df.dropna(subset=['Customer ID'], inplace=True)
    df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalSum'] = df['Quantity'] * df['Price']
    
    # 2. Aggregation (Turning Strings into Numbers)
    snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    
    rfm = df.groupby('Customer ID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recency
        'Invoice': 'nunique',                                    # Frequency
        'TotalSum': 'sum',                                       # Monetary
        'Description': 'nunique',                                # Diversity (String unique count)
        'Country': 'first'                                       # Country Tag
    })
    
    rfm.rename(columns={
        'InvoiceDate': 'Recency', 
        'Invoice': 'Frequency', 
        'TotalSum': 'Monetary', 
        'Description': 'Diversity'
    }, inplace=True)
    
    # 3. Categorical Encoding (Top 5 Countries + Other)
    top_countries = rfm['Country'].value_counts().nlargest(5).index
    rfm['Country'] = rfm['Country'].apply(lambda x: x if x in top_countries else 'Other')
    
    # Convert Country strings to 0/1 columns
    rfm = pd.get_dummies(rfm, columns=['Country'], prefix='C')
    
    return rfm