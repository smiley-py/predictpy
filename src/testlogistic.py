import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
import pandas as pd
from keras.layers import Dense

import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt


class CustomLogistic:
    def run(self):
        path = '/data/KidCreative.csv'

        data = pd.read_csv(path, delimiter=',')

        labels = data['Buy']
        features = data.iloc[:, 2:16]

        X = features
        y = np.ravel(labels)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.33, random_state=42)

        scaler = StandardScaler().fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)

        model = Sequential()
        model.add(Dense(8, activation='relu', input_shape=(14,)))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy',
                      optimizer='sgd',
                      metrics=['accuracy'])

        model.fit(X_train, y_train, epochs=8, batch_size=1, verbose=1)

        y_pred = model.predict(X_test)
        score = model.evaluate(X_test, y_test, verbose=1)
        print(score)
        # That’s to be expected as the accuracy of this model is 93.78%.

        df = pd.DataFrame(data, columns=np.array(data.columns))
        buyers = df.loc[(df.Buy == 1)]

        fig, ax = plt.subplots(2, 8, figsize=(16, 4))
        i = 0
        j = 0

        for c in buyers.columns[2:]:
            ax[j, i].hist(buyers[c])
            ax[j, i].set_title(c)
            i = i + 1
            if i == 8:
                j = 1
                i = 0

        fig.subplots_adjust(hspace=1, wspace=0.2)
        plt.show()

        df = pd.DataFrame(data, columns=data.columns)
        notbuyers = df.loc[(df.Buy == 0)]

        fig, ax = plt.subplots(2, 8, figsize=(16, 4))
        i = 0
        j = 0

        for c in np.array(data.columns)[2:]:
            ax[j, i].hist(notbuyers[c])
            ax[j, i].set_title(c)
            i = i + 1
            if i == 8:
                j = 1
                i = 0

        fig.subplots_adjust(hspace=1, wspace=0.2)
        plt.show()
