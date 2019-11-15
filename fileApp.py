from flask import Flask, request, jsonify
import os
import json
import csv
from werkzeug.utils import secure_filename

app = Flask(__name__)

data = {}
data['people'] = []
data['people'].append({
    '1': 'predicted_label',
    '2': 'predicted_label',
    '3': 'predicted_label',
    '4': 'predicted_label'
})



@app.route("/")
def hello_world():
    return "Hello World"

def helper(csvFile):
    return "book"

@app.route("/print_filename", methods=['POST','PUT'])
def print_filename():
    file = request.files['file']
    filename=secure_filename(file.filename)
    file.save(os.path.join('/Users/apurvabharatia/Desktop/uploads', filename))
    csvfile = open(os.path.join('/Users/apurvabharatia/Desktop/uploads', filename))
    res = helper(csvfile)
    jsonfile = open('file.json', 'w')
    fieldnames = ("Frames#",	"score_overall",	"nose_score",	"nose_x",	"nose_y",	"leftEye_score",	"leftEye_x",	"leftEye_y",
    "rightEye_score",	"rightEye_x"	"rightEye_y"	"leftEar_score",	"leftEar_x",	"leftEar_y",	"rightEar_score",	"rightEar_x",
    	"rightEar_y",	"leftShoulder_score",	"leftShoulder_x",
    "leftShoulder_y",	"rightShoulder_score",	"rightShoulder_x",	"rightShoulder_y",	"leftElbow_score",	"leftElbow_x",	"leftElbow_y",
    	"rightElbow_score",	"rightElbow_x",
    "rightElbow_y",	"leftWrist_score",	"leftWrist_x",	"leftWrist_y",	"rightWrist_score",	"rightWrist_x",	"rightWrist_y",	"leftHip_score",
    "leftHip_x",	"leftHip_y",	"rightHip_score",	"rightHip_x",	"rightHip_y",	"leftKnee_score",	"leftKnee_x"
    	"leftKnee_y",	"rightKnee_score",	"rightKnee_x",	"rightKnee_y",	"leftAnkle_score",	"leftAnkle_x",	"leftAnkle_y",	"rightAnkle_score",
        "rightAnkle_x",	"rightAnkle_y")
    #data = file.get_json()
    reader = csv.DictReader( csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')
    return jsonify(res)



if __name__=="__main__":
    app.run(port=5000, debug=True)
