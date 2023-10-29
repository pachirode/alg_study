from math import sqrt
from collections import Counter

import numpy as np

class KNNClassifier:
    def __init__(self, k) -> None:
        assert k >= 1, "k must be a positive integer"
        self._k = k
        self._x_train = None
        self._y_train = None

    def fit(self, x_train, y_train):
        assert x_train.shape[0] == y_train.shape[0], "x_train size must equal to y_train"
        assert self._k <= x_train.shape[0], "x_train size cannot smaller than k"
        self._x_train = x_train
        self._y_train = y_train
        return self

    def predict(self, predict_data):
        assert self._x_train is not None and self._y_train is not None, "please fit first"
        assert self._x_train.shape[1] == predict_data.shape[1], "perdict_data size must equal to x_train"
        return np.array([self._predict(data) for data in predict_data])

    def _predict(self, data):
        distances = [sqrt(np.sum((x - data) ** 2)) for x in self._x_train]
        nearest = [self._y_train[index] for index in np.argsort(distances[:self._k])]
        return Counter(nearest).most_common()[0][0]

