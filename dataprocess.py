import pandas as pd


df1 =  pd.read_csv('data/归一化的100hz SCL特征/filtered_scl_features.csv')
df2 =  pd.read_csv('data/归一化的100hz SCL特征/phasic_scl_features.csv')
df3 =  pd.read_csv('data/归一化的100hz SCL特征/tonic_scl_features.csv')


# 按照file 和 segment 合并
df = pd.merge(df1, df2, on=['File', 'Segment'])
df = pd.merge(df, df3, on=['File', 'Segment'])

df.to_csv('data/归一化的100hz SCL特征/merged_scl_features.csv', index=False)
