import numpy as np
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
from sklearn.metrics import auc
from sklearn.metrics import roc_curve
from scipy import interp
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from scikitplot.metrics import plot_confusion_matrix


def baseline_model():
  # create model
  model = Sequential()
  model.add(Dense(500, activation='relu', input_dim=6))
  model.add(Dense(200, activation='relu'))
  model.add(Dense(100, activation='relu'))
  model.add(Dense(2, activation='softmax'))

  # Compile model
  model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
  return model

seed = 7
numpy.random.seed(seed)

n_classes = 2

dataframe = pandas.read_csv("dataset.csv", header=None,sep = ",")

#data = pandas.read_csv('dataset.csv', usecols = ['distanza','distanzaDx','distanzaSx'])
#predict = pandas.read_csv('dataset.csv', usecols = ['Sesso'])

dataset = dataframe.values

X = dataset[:,0:6]
Y = dataset[:,6]
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

Y = dummy_y

dummy_x = X
print(dummy_x)

print(Y)

X_train, X_test, y_train, y_test = train_test_split(dummy_x,Y, test_size = 0.3)

print('Calcolo...')


keras_model = baseline_model()
history = keras_model.fit(X_train, y_train, epochs = 100, batch_size = 331, verbose = 1,validation_split=0.33)

y_score = keras_model.predict(X_test)
score = keras_model.evaluate(X_test, y_test, verbose=0)
score1 = keras_model.evaluate(X_train, y_train, verbose=0)


predictions = keras_model.predict_classes(X_test)

#for i in range(len(X_test)):
#	print('(Prediction %d) => (expected %s)' % (predictions[i], y_test[i]))

print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


test = []
predict = []

for i in range(len(X_test)):
	test.append(y_test[i])
	predict.append(predictions[i])

#print(confusion_matrix(test,predict))
print("Accuracy Train: %.2f%%" % (score1[1]*100))
print("Accuracy Test: %.2f%%" % (score[1]*100))