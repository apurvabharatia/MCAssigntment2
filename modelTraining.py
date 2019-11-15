import pandas as pd

bookData = pd.read_pickle("bookData")
print(type(bookData))

print(bookData.loc[3])

val = list(bookData.loc[3])

print(len(val))

label = 0
bookDatanew = []

print(len(bookData))
for i in range(len(bookData)):
    currRow = bookData.loc[i]
    vals = list(currRow)[0].split(",")
    vals = vals[2:]

    xVals = []
    yVals = []
    for i in range(1, len(vals), 3):
        xVals.append(vals[i])
    for i in range(2, len(vals), 3):
        yVals.append(vals[i])

    xMin = min(xVals)
    xMax = max(xVals)
    yMin = min(yVals)
    yMax = max(yVals)
    newXVals = []
    for i in range(len(xVals)):
        currVal = xVals[i]
        currVal = (currVal - xMin) / (xMax - xMin)
        newXVals.append(currVal)
    newYVals = []
    for i in range(len(yVals)):
        currVal = yVals[i]
        currVal = (currVal - yMin) / (yMax - yMin)
        newYVals.append(currVal)
    newRow = []
    for val in newXVals:
        newRow.append(val)
    for val in newYVals:
        newRow.append(val)
    newRow.append(label)

    bookDatanew.append(newRow)