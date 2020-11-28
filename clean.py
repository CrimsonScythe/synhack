from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

df=pd.read_csv('synthetic_data.csv')
# sns.heatmap(df.corr(), annot=True)
# plt.show()

'''onehot'''
y=pd.get_dummies(df, columns=['race', 'gender', 'age', 'max_glu_serum', 'A1Cresult', 'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'acetohexamide', 'glipizide',
       'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose',
       'miglitol', 'troglitazone', 'tolazamide', 'examide', 'citoglipton',
       'insulin', 'glyburide-metformin', 'glipizide-metformin',
       'glimepiride-pioglitazone', 'metformin-rosiglitazone',
       'metformin-pioglitazone', 'change', 'diabetesMed', '_diag_1', '_diag_2', '_diag_3'])
y.to_csv('synthetic_data_dum1.csv')
# '''label encoder'''
# le = preprocessing.LabelEncoder()
# df[''] = le.fit_transform(df[''])
