import numpy as np
import pandas as pd

def format_column(df: pd.DataFrame):
    '''Change title of columns'''
    df.columns = df.columns.str.upper()
    df.columns = df.columns.str.replace('(','', regex=False)
    df.columns = df.columns.str.replace(')','', regex=False)
    df.columns = df.columns.str.replace(' ','_', regex=False)

    return df


def feature_engineering(df: pd.DataFrame):
    '''Create new columns and return separately X and y'''
    orig_feat_names_list = df.columns[:4].tolist()

    for i in orig_feat_names_list:
        df[i + '_GROUP'] = np.select(
            [
                df[i] <= df[i].quantile(0.25),
                (df[i] > df[i].quantile(0.25)) & (df[i] <= df[i].quantile(0.5)),
                (df[i] > df[i].quantile(0.5)) & (df[i] <= df[i].quantile(0.75)),
                df[i] > df[i].quantile(0.75),
            ], [1,2,3,4], np.nan
        )
    
    X = df.drop(columns=['TARGET'])
    y = df['TARGET']

    return X, y