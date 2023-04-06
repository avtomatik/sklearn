# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
from data.make_dataset import get_data_frame, get_X_y
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV, train_test_split

X, y = get_data_frame().pipe(get_X_y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.4, random_state=0)


lasso = Lasso(random_state=42)
param_grid = {'alpha': np.linspace(0, 1, 10)}
gscv = GridSearchCV(estimator=lasso, param_grid=param_grid, cv=10, verbose=2)
gscv.fit(X_train, y_train)
gscv.best_params_
model = gscv.best_estimator_

model.fit(X_train, y_train)
model.score(X_test, y_test)
prediction = model.predict(X_test)


# =============================================================================
# usa_cobb_douglas0014.py
# =============================================================================
# =============================================================================
# TODO: Revise Fixed Assets Turnover Approximation with Lasso
# =============================================================================
print(get_data_frame().pipe(get_data_frame_transformed).iloc[:, [6]])
