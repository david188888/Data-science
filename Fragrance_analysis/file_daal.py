import pandas as pd


df = pd.read_csv('data/总表.csv')



df['age'] = df['age'].fillna(method='ffill')
df['sex'] = df['sex'].fillna(method='ffill')

df.to_csv('data/new_table.csv', index=False)  # index=False 表示不保存索引列