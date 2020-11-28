from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df=pd.read_csv('synthetic_data.csv')
y=pd.get_dummies(df)
y.to_csv('synthetic_data_dum.csv')