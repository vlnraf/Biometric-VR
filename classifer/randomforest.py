import pandas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from scikitplot.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt

data = pandas.read_csv('../dati/datiCompleti/dataset1.csv', usecols = ['distanza','altezza','distanzaDx','distanzaSx'])
predict = pandas.read_csv('../dati/datiCompleti/dataset1.csv', usecols = ['Sesso'])

X = data
y = predict


X_train,X_test,y_train,y_test = train_test_split(X,y.values.ravel(), test_size = 0.3)

model = RandomForestClassifier()
model.fit(X_train,y_train)

p_train = model.predict(X_train)
p_test = model.predict(X_test)

acc_train = accuracy_score(y_train, p_train)
acc_test = accuracy_score(y_test, p_test)

plot_confusion_matrix(y_test, p_test)

plt.show()

print(confusion_matrix(y_test, p_test))

print( f'Train {acc_train}, test {acc_test}')
