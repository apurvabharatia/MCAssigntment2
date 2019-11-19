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



if __name__ == '__main__':
 	test_data = pd.read_pickle("t_x.pkl")
 	print(test_data.shape)
 	class1 = Random_Forest(test_data)
 	class2 = knn(test_data)
 	class3 = decision_tree(test_data)
 	class4 = logistic_regression(test_data)

 	print(class1)
 	print(class2)
 	print(class3)
 	print(class4)