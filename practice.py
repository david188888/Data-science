from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import featuretools as ft

dataset = load_iris()
X = dataset.data
y = dataset.target
iris_feature_names = dataset.feature_names

df = pd.DataFrame(X, columns=iris_feature_names)

print(df.head())

import featuretools as ft
es = ft.EntitySet(id='single_dataframe')  # 用id标识实体集
# 增加一个数据框，命名为iris
es.add_dataframe(dataframe_name='iris', dataframe=df, index='index')

trans_primitives=['add_numeric', 'subtract_numeric', 'multiply_numeric', 'divide_numeric']  # 2列相加减乘除来生成新特征
# ft.list_primitives()  # 查看可使用的特征集元
feature_matrix, feature_names = ft.dfs(entityset=es, 
     target_dataframe_name='iris', 
     max_depth=1,    # max_depth=1，只在原特征上进行运算产生新特征
     verbose=1,
     trans_primitives=trans_primitives
)

print(feature_matrix.head())

