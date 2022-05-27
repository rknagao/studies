import pandas as pd
from sklearn.model_selection import train_test_split

def preprocessing(X, y):
    '''Separate the train and test from original sample and save copies'''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    #savind proprocessed data
    df_train = pd.concat([X_train, y_train], axis=1)
    df_train.to_csv('./data/preprocessed_train_data.csv', index=False)
    df_test = pd.concat([X_test, y_test], axis=1)
    df_test.to_csv('./data/preprocessed_test_data.csv', index=False)

    return X_train, X_test, y_train, y_test