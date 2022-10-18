import sklearn
import pandas as pd
import numpy as np

from sklearn import datasets  # import the datasets module

dataset = datasets.load_breast_cancer(as_frame=True) # Download the dataset:
read_dataset = pd.read_csv(dataset)
print(read_dataset.describe())
print('Targets:', dataset.target_names)
print('Features:', dataset.feature_names)

target = dataset.target
print(target.unique()) #查找target欄不重複的數量

features = dataset.data
print(features.head(5))

print(target.value_counts())

