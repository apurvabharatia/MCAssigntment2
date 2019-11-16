import pandas as pd
import random


df = pd.read_pickle("book.pkl")
dfTrain = pd.DataFrame(columns = df.columns)
dfTest = pd.DataFrame(columns = df.columns)
train = 0
test = 0

labels = ["book", "car", "gift", "movie", "sell", "total"]
for label in labels:
    df = pd.read_pickle(label + ".pkl")

    l, w = df.shape
    trainLen = int(l) * 0.7

    i = 0
    v = set()

    while i < trainLen + 1:
        ind = random.randrange(l)
        if ind not in v:
            dfTrain.loc[train] = df.iloc[ind]
            train += 1
            i += 1
            v.add(ind)
    s = set([i for i in range(l)]) - v
    i = 0
    for j in s:
        dfTest.loc[test] = df.iloc[j]
        test += 1

dfTrain.to_pickle("trainingData.pkl")
dfTest.to_pickle("testingData.pkl")
