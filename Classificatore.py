import pandas
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pandas.read_csv('dati/datiCompleti/dataset.csv', usecols = ['distanza','distanzaDx','distanzaSx'])
predict = pandas.read_csv('dati/datiCompleti/dataset.csv', usecols = ['Sesso'])

X = data
y = predict


X_train,X_test,y_train,y_test = train_test_split(X,y)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

p_train = model.predict(X_train)
p_test = model.predict(X_test)
prob = model.predict_proba(X_train)
probability = model.predict_proba(X_test)

acc_train = accuracy_score(y_train, p_train)
acc_test = accuracy_score(y_test, p_test)

#print( f'Train {acc_train}, test {acc_test}')
print( f'Train {prob}, test {probability}')

