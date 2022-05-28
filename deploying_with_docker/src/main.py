from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
from script1_extract import extract
from script2_feature_engineering import format_column, feature_engineering
from script3_preprocessing import preprocessing
from script4_model import model
from script5_metric import metric

if __name__ == '__main__':

    #ETL
    df = extract()
    df = format_column(df)
    X, y = feature_engineering(df)
    
    #PREPROCESSING
    X_train, X_test, y_train, y_test = preprocessing(X, y)
    
    #MODEL
    y_pred = model(X_train, y_train, X_test)
    result = metric(y_test, y_pred)

    print(result)
    print('end')