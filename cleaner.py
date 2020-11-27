import pandas as pd, numpy as np
import os

def clean_file(filename): #return clean dataframe
    df = pd.read_csv('./data/' + filename, sep=',')
    df.columns = [col.lower() for col in df.columns]
    df = df.query('date >= "2015-01-01"')
    return df

def save_file(df, filename): #create csv file in (temporary) subdirectory
    df.to_csv('data_clean/' + filename, index=False)

for filename in os.listdir('data'):
    df = clean_file(filename)
    save_file(df, filename)
