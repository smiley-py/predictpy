import tensorflow as tf
from keras.models import Sequential
import pandas as pd
from keras.layers import Dense

import seaborn as sns
import matplotlib as plt

import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from keras.utils import plot_model


class CustomDiabetes:
    def run(self):
        data = pd.read_csv(
            '/data/diabetes.csv', delimiter=',')
        # data.describe()
        # data.info()

        corr = data.corr()
        sns.heatmap(corr, xticklabels=corr.columns.values,
                    yticklabels=corr.columns.values)

        data['BloodPressure'].corr(data["BMI"])
        # 0.2818052888499106
        data["Pregnancies"].corr(data["Age"])
        # 0.5443412284023394

        labels = data['Outcome']
        features = data.iloc[:, 0:8]

        X = features
        y = np.ravel(labels)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.33, random_state=42)

        scaler = StandardScaler().fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)

        model = Sequential()
        model.add(Dense(8, activation='relu', input_shape=(8,)))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(loss='binary_crossentropy',
                      optimizer='sgd',
                      metrics=['accuracy'])

        model.fit(X_train, y_train, epochs=4, batch_size=1, verbose=1)

        for layer in model.layers:
            weights = layer.get_weights()

        plot_model(model, to_file='/tmp/model.png', show_shapes=True,)

        y_pred = model.predict_classes(X_test)

        score = model.evaluate(X_test, y_test, verbose=1)
        print(score)
        # So, our predictive model is 72% accurate.
