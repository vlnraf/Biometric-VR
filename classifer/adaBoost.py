import pandas
from sklearn import model_selection
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import LeavePOut
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from scikitplot.metrics import plot_confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

data = pandas.read_csv('../dati/datiCompleti/dataset1.csv', usecols = ['distanza','altezza','distanzaDx','distanzaSx'])
predict = pandas.read_csv('../dati/datiCompleti/dataset1.csv', usecols = ['Sesso'])

scores=[]

X = data.values
y = predict.values.ravel()
#loo = LeaveOneOut()
#loo.get_n_splits(X)

#cv = KFold(n_splits=30)
#cv.get_n_splits(X)

#print(cv)
#KFold(n_splits=30, random_state=None, shuffle=False)

#for train, test in loo.split(X):
#    print("TRAIN:", train, "TEST:", test)
#    X_train, X_test = X[train], X[test]
#    y_train, y_test = y[train], y[test]
#    print(X_train, X_test, y_train, y_test)

#for train_index, test_index in cv.split(X):
#    print("Train Index: ", train_index, "\n")
#    print("Test Index: ", test_index)


#X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
model = AdaBoostClassifier()

kfold = model_selection.KFold(n_splits=30, shuffle=False)
model_kfold = AdaBoostClassifier()
results_kfold = model_selection.cross_val_score(model, X, y, cv=kfold)
print("Accuracy: %.2f%%" % (results_kfold.mean()*100.0)) 

#for i in range(len(X_test)):
#    print('(Prediction %d) => (expected %s)' % (predictions[i], y_    test[i]))

#model.fit(X_train, y_train)
#scores.append(model.score(X_test, y_test))

#print(np.mean(scores))

#cross_val_predict(model, X, y, cv=10)


#X_train,X_test,y_train,y_test = train_test_split(X,y.values.ravel(), test_size = 0.3)
#
#model = AdaBoostClassifier()
#model.fit(X_train,y_train)
#model.score(X_train, y_train)

#p_train = model.predict(X_train)
#p_test = model.predict(X_test)
#
#acc_train = accuracy_score(y_train, p_train)
#acc_test = accuracy_score(y_test, p_test)
#
#plot_confusion_matrix(y_test, p_test)
#
#plt.show()
#
#print(confusion_matrix(y_test, p_test))
#
#print( f'Train {acc_train}, test {acc_test}')

