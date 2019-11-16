# importing csv module 
import csv 
from os import listdir
from os.path import isfile, join 
import pandas as pd 


dic = {
    "book": 0,
    "car": 1,
    "gift": 2,
    "movie": 3,
    "sell": 4,
    "total": 5
}
# csv file name 
label = "book"
opfilename = "./CSV_Thursday/CSV/" + label + "_features/"
onlyfiles = [f for f in listdir(opfilename)]
with open(opfilename + onlyfiles[0], 'r') as a:
    csvreader = csv.reader(a) 
    fields = next(csvreader) 
fields.append('label')
df = pd.DataFrame(columns = fields)
for ind, f in enumerate(onlyfiles):
    # reading csv file 
    fields = []
    rows = []
    with open(opfilename + f, 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        fields = next(csvreader) 
    
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
    
        # get total number of rows 
        # print("Total no. of rows: %d"%(csvreader.line_num)) 
    
    # printing the field names 
    # print('Field names are:' + ', '.join(field for field in fields)) 
    # print(len(rows), len(rows[0]), len(rows[-1]))
    #print(df.shape)
    res = [0] * len(fields)
    for row in rows:
        for i, val in enumerate(row):
            res[i] += float(val)

    for i, val in enumerate(res):
        res[i] = val / len(rows)
    fields.append('label')
    res.append(dic[label])
    df.loc[ind] = res

df.to_pickle(label + ".pkl")