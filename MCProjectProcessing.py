import csv
import pandas as pd
import xlrd
import glob, os

fileName = "/Users/apurvabharatia/Desktop/MC/MC Project/Crime log data/April2017.xlsx"
configfiles = glob.glob('/Users/apurvabharatia/Desktop/MC/MC Project/Crime log data')
data = []

outer = "/Users/apurvabharatia/Desktop/MC/MC Project/Crime log data/"

os.chdir("/Users/apurvabharatia/Desktop/MC/MC Project/Crime log data/")

"""
for file in glob.glob("*.xlsx"):
    print(file)
"""

for file in glob.glob("*.xlsx"):
    print("file: ", file)
    loc = outer + file

    # Give the location of the file
    #loc = ("/Users/apurvabharatia/Desktop/MC/MC Project/Crime log data/April2017.xlsx")
    try:
        # To open Workbook
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)

        # For row 0 and column 0


        count = 0
        Locations = {}
        for i in range(sheet.nrows):
            currRow = sheet.row(i)

            if sheet.cell_value(i, 0) != '' and sheet.cell_value(i, 1) != '' and sheet.cell_value(i, 2) != '' and sheet.cell_value(i, 3) != '' and sheet.cell_value(i, 4) != '' and sheet.cell_value(i, 5) != '' and sheet.cell_value(i, 6) != '' and sheet.cell_value(i, 7) != '' and sheet.cell_value(i, 8) != '' and sheet.cell_value(i, 9) != '':
                    #print(sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2), sheet.cell_value(i, 3),sheet.cell_value(i, 4), sheet.cell_value(i, 5), sheet.cell_value(i, 6), sheet.cell_value(i, 7), sheet.cell_value(i, 8), sheet.cell_value(i, 9))
                    incidentNo, dateRep, timeRep, dateFrom, timeFrom, dateTo, timeTo, desc, location, desposition = sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2), sheet.cell_value(i, 3), sheet.cell_value(i, 4), sheet.cell_value(i, 5), sheet.cell_value(i, 6), sheet.cell_value(i, 7), sheet.cell_value(i, 8), sheet.cell_value(i, 9)
                    #print("LOCATION: ", location)
                    if location in Locations:
                        Locations[location] += 1
                    else:
                        Locations[location] = 1
                    #if incidentNo & dateRep & timeRep & dateFrom & timeFrom & dateTo & timeTo & desc & loc & desposition:
                    data.append([str(incidentNo), str(dateRep), str(timeRep), str(dateFrom), str(timeFrom), str(dateTo), str(timeTo), str(desc), str(location), str(desposition)])
                    data.append((['']))

            count += 1
    except:
            print("Oops")

#print(count)
#print(Locations)
print(len(data))
print((Locations))

for key, value in Locations.items():
    print(key, value)