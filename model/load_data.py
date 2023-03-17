# _*_ coding : utf-8 _*_
# @Time : 2023/3/13 11:01
# @Author : Black
# @File : load_data
# @Project : Mel_recognition

import pandas as pd
import numpy as np


def feature_normalize(dataset):
    mu = np.mean(dataset, axis=0)
    sigma = np.std(dataset, axis=0)
    return (dataset - mu) / sigma


def load_train(path, columns):
    dataset = pd.read_excel(path)
    train_X = feature_normalize(dataset[columns])
    # train_X = feature_normalize(dataset[columns])
    train_y = dataset['score']
    return train_X, train_y


def load_test(path, columns):
    dataset = pd.read_excel(path)
    test_X = feature_normalize(dataset[columns])
    # test_X = feature_normalize(dataset[columns])
    test_y = dataset['score']
    return test_X, test_y
