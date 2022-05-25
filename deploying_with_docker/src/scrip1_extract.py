from sklearn.datasets import load_iris
import numpy as np
import pandas as pd


def extract():
    '''Extract the Iris dataset from sklearn and return a dataframe'''
    data = load_iris()
    df = pd.DataFrame(np.concatenate((iris.data, np.array([iris.target]).T), axis=1), columns=iris.feature_names + ['target'])
    
    return df