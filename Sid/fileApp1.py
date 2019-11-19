from flask import Flask, request, jsonify
import os
import json
import csv
import ast
from preprocessData import preprocess
from werkzeug.utils import secure_filename
from svm import genericSVM

app = Flask(__name__)



import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pickle
from sklearn.metrics import confusion_matrix, classification_report,accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA

dict1 = {0:"book",1:"car",2:"gift",3:"movie",4:"sell",5:"total"}

def return_PCA_features(test_data,n):
    X_train = pd.read_pickle("train_x.pkl")
    Y_train = pd.read_pickle('train_y.pkl')
    new = [X_train,test_data]
    X_trainPCA = pd.concat(new)
    pca = PCA(n)
    pca.fit(X_trainPCA)

    X_train1 = pca.transform(X_trainPCA)
    print(X_train1.shape)
    test = X_train1[X_train1.shape[0]-1]
    return(test)

def Random_Forest(test_data):
    
    test = return_PCA_features(test_data,7)
    #print(test)
    #X_test1 = pca.transform(test_data)
    #print("X_test.shape: "+str(X_test1.shape))
    RF_model = pd.read_pickle("Random_Forest_Model.pickle")
    Pred = RF_model.predict(test.reshape(1,-1))
    #print("Pred.shape"+str(Pred.shape))
    for i in Pred:
        class1 = int(i)
    
    return dict1[class1]

def knn(test_data):
    test = return_PCA_features(test_data,7)
    model = pd.read_pickle("KNN_Model.pickle")
    Pred = model.predict(test.reshape(1,-1))
    for i in Pred:
        class1 = int(i)
    
    return dict1[class1]


    #return(Pred)

def decision_tree(test_data):
    test = return_PCA_features(test_data,14)
    model = pd.read_pickle("DecisionTree_Model.pickle")
    Pred = model.predict(test.reshape(1,-1))
    for i in Pred:
        class1 = int(i)
    
    return dict1[class1]

def logistic_regression(test_data):
    test = return_PCA_features(test_data,12)
    model = pd.read_pickle("LogisticRegression_Model.pickle")
    Pred = model.predict(test.reshape(1,-1))
    for i in Pred:
        class1 = int(i)
    
    return dict1[class1]



@app.route("/")
def hello_world():
    return "Hello World"

def helper(csvFile):
    return "book"

@app.route("/print_filename", methods=['POST','PUT'])
def print_filename():
    # file = request.files['file']
    payLoad = request.get_json()
    print(payLoad)
    l = ast.literal_eval(payLoad["logMessage"])
    #logMessage = json.loads(payLoad["logMessage"])
    preprocess(l)
    # filename=secure_filename(file.filename)
    # file.save(os.path.join('/Users/apurvabharatia/Desktop/uploads', filename))
    # csvfile = open(os.path.join('/Users/apurvabharatia/Desktop/uploads', filename))
    test_data = pd.read_pickle("t_x.pkl")
    class1 = Random_Forest(test_data)
    class2 = knn(test_data)
    class3 = decision_tree(test_data)
    class4 = logistic_regression(test_data)

    #print(class1)
    #print(class2)
    #print(class3)
    #print(class4)
    # jsonfile = open('file.json', 'w')
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
    # reader = csv.DictReader( csvfile, fieldnames)
    # for row in reader:
    #     json.dump(row, jsonfile)
    #     jsonfile.write('\n')
    return jsonify({"1": class1, "2":class2,"3":class3,"4":class4})



if __name__=="__main__":
    app.run(port=5000, debug=True)
