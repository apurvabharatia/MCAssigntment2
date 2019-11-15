import numpy as np
import cvxopt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
import glob, os
import pandas as pd
import pickle


configfiles = glob.glob('/Users/apurvabharatia/Desktop/MC/CSV/total')

os.chdir("/Users/apurvabharatia/Desktop/MC/CSV/total")

folders = ["book", "car", "gift", "movie", "sell", "total"]

"""
label key:

book   = 0
car    = 1
gift   = 2
movie  = 3
sell   = 4
total  = 5 

"""

"""
for f in folders:
    currconfigfile = configfiles + f
    os.chdir(currconfigfile)
"""
outer = "/Users/apurvabharatia/Desktop/MC/CSV/total/"

bookData = []

for file in glob.glob("*.csv"):
    with open(outer + file, "r") as currCsv:
        lineCount = 0
        for row in currCsv:
            bookData.append(row)
            lineCount += 1
        print("file: ", file, "lines: ", lineCount)

print(len(bookData))
bookData = pd.DataFrame(bookData)
bookData.to_pickle("/Users/apurvabharatia/Desktop/MC/CSV/totalData")


"""
/Users/apurvabharatia/Desktop/MC/CSV/book/BOOK_PRACTICE_1_DAVE.csv
"""

