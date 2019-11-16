# importing csv module 
import csv 
from os import listdir
from os.path import isfile, join  


# csv file name 
feature = "sell"
filename = "./CSV_Thursday/CSV/" + feature + "/"
opfilename = "./CSV_Thursday/CSV/" + feature +"_features/"
onlyfiles = [f for f in listdir(filename)]


# initializing the titles and rows list 

for f in onlyfiles:
    fields = [] 
    rows = [] 
    # reading csv file 
    with open(filename + f, 'r') as csvfile: 
        # creating a csv reader object 
        print(csvfile)
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        fields = next(csvreader) 
    
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
    
        # get total number of rows 
        print("Total no. of rows: %d"%(csvreader.line_num)) 
    
    # printing the field names 
    print('Field names are:' + ', '.join(field for field in fields)) 

    x_fields, y_fields, x_cols, y_cols = [], [], [], []
    print("Important rows")
    impFields = []
    for i, field in enumerate(fields):
        if "_x" in field:
            x_fields.append(field)
            x_cols.append(i)
            impFields.append(field)
        if "_y" in field:
            y_fields.append(field)
            y_cols.append(i)
            impFields.append(field)
    x_cols = x_cols[:-2]
    y_cols = y_cols[:-2]
    impFields = impFields[:-4]
    fileValues = []
    print(len(rows))
    for frame in rows:
        x_min, y_min, x_max, y_max = float("inf"), float("inf"), float("-inf"), float("-inf")
        for x_col, y_col in zip(x_cols, y_cols):
            x_min = min(x_min, float(frame[x_col]))
            y_min = min(y_min, float(frame[y_col]))
            x_max = max(x_max, float(frame[x_col]))
            y_max = max(y_max, float(frame[y_col]))

        x_values, y_values = [], []
        impValues = []
        for x_col, y_col in zip(x_cols, y_cols):
            x_values.append((float(frame[x_col]) - x_min) / (x_max - x_min))
            y_values.append((float(frame[y_col]) - y_min) / (y_max - y_min))
            impValues.append(x_values[-1])
            impValues.append(y_values[-1])
        fileValues.append(impValues[:])
    with open(opfilename + f, "w") as csv_file:
        csv_file.write(','.join(impFields) + '\n')
        for line in fileValues:
            csv_file.write(','.join([str(l) for l in line]) + '\n')
    