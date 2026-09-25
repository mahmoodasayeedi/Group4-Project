import pandas as pd


def load():
  
    df =pd.read_csv('../data/sales.csv')
    
    return df