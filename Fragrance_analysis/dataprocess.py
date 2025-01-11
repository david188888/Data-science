import pandas as pd


df1 = pd.read_excel('Fragrance_analysis/data/experiment.xlsx')
df2 = pd.read_csv('Fragrance_analysis/data/new_table.csv')


# 选择'试次'，'P1', 'A1', 'D1', 'P2', 'A2', 'D2', 'P3', 'A3', 'D3' 这几列

df1 = df1[['试次', 'P1', 'A1', 'D1', 'P2', 'A2', 'D2', 'P3', 'A3', 'D3']]

# 将df1的试次列名改为file
df1.rename(columns={'试次': 'file'}, inplace=True)

df = pd.merge(df1, df2, on='file')

df.to_csv('Fragrance_analysis/data/new_table.csv', index=False)