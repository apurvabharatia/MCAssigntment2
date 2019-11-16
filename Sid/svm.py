from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

# loading the iris dataset
iris = datasets.load_iris()

# X -> features, y -> label
X = iris.data
print("type X: ", X.shape)

y = iris.target
print("type y: ", y.shape)




# dividing X, y into train and test data
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
X_train = pd.read_pickle('train_x.pkl').to_numpy()
Y_train = pd.read_pickle('train_y.pkl').to_numpy()
X_test = pd.read_pickle('test_x.pkl').to_numpy()
Y_test = pd.read_pickle('test_y.pkl').to_numpy()
# training a linear SVM classifier
from sklearn.svm import SVC

svm_model_linear = SVC(kernel='linear', C=1).fit(X_train, Y_train)
svm_predictions = svm_model_linear.predict(X_test)

# model accuracy for X_test
accuracy = svm_model_linear.score(X_test, Y_test)

# creating a confusion matrix
cm = confusion_matrix(Y_test, svm_predictions)

print(accuracy)