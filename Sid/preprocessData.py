# importing csv module 
import csv 
from os import listdir
from os.path import isfile, join  
import pandas as pd


def preprocess(jsonData):

    parts = {
        "nose": 0,
        "leftEye": 2,
        "rightEye": 4,
        "leftEar": 6,
        "rightEar": 8,
        "leftShoulder": 10,
        "rightShoulder": 12,
        "leftElbow": 14,
        "rightElbow": 16,
        "leftWrist": 18,
        "rightWrist": 20,
        "leftHip": 22,
        "rightHip": 24,
        "leftKnee": 26,
        "rightKnee": 28
    }

    f = 'book_1_narvekar.csv'
    fields = [] 
    rows = [] 
    # reading csv file 
    with open(f, 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        fields = next(csvreader) 

    x_fields, y_fields, x_cols, y_cols = [], [], [], []
    impFields = []
    indices = []
    j = 0
    for i, field in enumerate(fields):
        if "_x" in field:
            indices.append(j)
            x_cols.append(i)
            impFields.append(field)
            j += 1
        if "_y" in field:
            indices.append(j)
            y_fields.append(field)
            y_cols.append(i)
            impFields.append(field)
            j += 1
    x_cols = x_cols[:-2]
    y_cols = y_cols[:-2]
    impFields = impFields[:-4]
    fileValues = []
    impValues = [0] * len(impFields)
    for frame in jsonData:
        x_min, y_min, x_max, y_max = float("inf"), float("inf"), float("-inf"), float("-inf")
        keypoints = frame["keypoints"]
        frameValues = [0] * len(impFields)
        for keypoint in keypoints:
            part = keypoint["part"]
            if part in parts and not "Ankle" in parts:
                frameValues[parts[part]] = keypoint['position']['x']
                frameValues[parts[part] + 1] = keypoint['position']['y']
        
        for i, val in enumerate(frameValues):
            if i % 2 == 0:
                x_min = min(x_min, val)
                x_max = max(x_max, val)
            else:
                y_min = min(y_min, val)
                y_max = max(y_max, val)

        for i, val in enumerate(frameValues):
            if i % 2 == 0:
                frameValues[i] = ((val - x_min) / (x_max - x_min))
            else:
                frameValues[i] = ((val - y_min) / (y_max - y_min))

        fileValues.append(frameValues[:])
    with open("sample1.csv", "w") as csv_file:
        csv_file.write(','.join(impFields) + '\n')
        for line in fileValues:
            csv_file.write(','.join([str(l) for l in line]) + '\n')
    vectorForm("sample1.csv")
        
def vectorForm(f):
    dic = {
        "book": 0,
        "car": 1,
        "gift": 2,
        "movie": 3,
        "sell": 4,
        "total": 5
    }
    label = "sample1"
    fields = []
    rows = []
    ind = 0
    with open(f, 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        fields = next(csvreader) 
    
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
    
    res = [0] * len(fields)
    for row in rows:
        for i, val in enumerate(row):
            res[i] += float(val)

    for i, val in enumerate(res):
        res[i] = val / len(rows)
    df = pd.DataFrame(columns = fields)
    df.loc[ind] = res

    df.to_pickle(label + "_server_test.pkl")
    test_server("sample1_server_test.pkl")

def test_server(filename):
	t = pd.read_pickle(filename)
	x_tr, y_tr = t.shape
	#t_y = t.iloc[0: x_tr, y_tr - 1: y_tr]
	t_x = t.iloc[0: x_tr, 0: y_tr]
	t_x.to_pickle("t_x.pkl")
	#t_y.to_pickle("t_y.pkl")