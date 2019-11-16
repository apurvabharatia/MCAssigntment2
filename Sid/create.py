import pandas as pd
import random


train = pd.read_pickle("trainingData.pkl")
test = pd.read_pickle("testingData.pkl")
x_tr, y_tr = train.shape
train_y = train.iloc[0: x_tr,  y_tr - 1: y_tr]
train_x = train.iloc[0: x_tr, 0: y_tr - 1]
x_tr, y_tr = test.shape
test_y = test.iloc[0: x_tr,  y_tr - 1: y_tr]
test_x = test.iloc[0: x_tr, 0: y_tr - 1]

print(train_x.shape)
print(train_y.shape)
print(test_x.shape)
print(test_y.shape)

train_x.to_pickle("train_x.pkl")
train_y.to_pickle("train_y.pkl")
test_x.to_pickle("test_x.pkl")
test_y.to_pickle("test_y.pkl")