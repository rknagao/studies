import pandas as pd
import pickle
from sklearn import tree

def model(X_train, y_train, X_test):
    '''Training and testing a DecisionTreeClassifier model with X, y'''

    model = tree.DecisionTreeClassifier().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # save the model to disk
    pickle.dump(model, open('./model/model_tree_iris.sav', 'wb'))
        
    return y_pred











