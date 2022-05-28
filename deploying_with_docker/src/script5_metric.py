import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score

def metric(y, y_pred):
    '''To calculate accuracy, precision, recall and roc'''

    acc = accuracy_score(y, y_pred).round(3)
    prec = precision_score(y, y_pred, average="macro").round(3)
    rec = recall_score(y, y_pred, average="macro").round(3)
    result = pd.Series(data=[acc, prec, rec], index=['accuracy','precision', 'recall'])

    return result