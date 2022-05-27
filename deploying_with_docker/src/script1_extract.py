from sklearn.datasets import load_iris
import pandas as pd


def extract():
    '''Extract the Iris dataset from sklearn and return a dataframe'''
    data = load_iris()
    df = pd.DataFrame(data=data['data'], columns=data['feature_names'])
    df['target'] = data['target']

    #saving original dataset
    df.to_csv('./data/raw_data.csv', index=False)
    return df