from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
from script1_extract import extract
from script2_feature_engineering import format_column, feature_engineering
from script3_preprocessing import preprocessing
from script4_model import model

if __name__ == '__main__':

    #ETL
    df = extract()
    df = format_column(df)
    X, y = feature_engineering(df)
    
    #MODEL
    X_train, y_train, X_test, y_test = preprocessing(X, y)

    #TRAIN
    y_pred = model(X_train, y_train, X_test)
    (RETUNRANDO ERRO)

    print(df.sample(3))
    print('end')