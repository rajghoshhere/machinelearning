# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:13:14 2021

@author: RPTWR6V
"""

import numpy as nump
import matplotlib.pyplot as plot
import pandas as pd
import sklearn as sk

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)