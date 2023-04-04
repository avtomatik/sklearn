# =============================================================================
# Test:
# https://stackoverflow.com/questions/49522928/cross-validation-in-linear-regression
# https://scikit-learn.org/stable/tutorial/statistical_inference/model_selection.html
# https://scikit-learn.org/stable/auto_examples/exercises/plot_cv_diabetes.html
# =============================================================================
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import (KFold, LeaveOneOut, ShuffleSplit,
                                     cross_val_score, train_test_split)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
# =============================================================================
# Support Vector Machine
# =============================================================================
from sklearn.svm import SVC

import sklearn
from data.collect import stockpile_cobb_douglas
from data.transform import transform_cobb_douglas

# =============================================================================
# Labor Capital Intensity
# Labor Productivity
# =============================================================================
X, y = get_data_frame().pipe(get_X_y)

# X = np.transpose(np.atleast_2d(X))  # Required


# loo = LeaveOneOut(y.shape[0])
# regr = LinearRegression()
## scores = cross_val_score(regr, X, y, scoring='mean_squared_error', cv=loo)
# print(scores.mean())
# lr = LinearRegression()
# lr.fit(X, y)
# =============================================================================
# r2 = lr.score(X, y)
# =============================================================================
# r2 = r2_score(y, lr.predict(X))

#### print("R2 (test data): {:.2}".format(r2))
#### kf = KFold(len(X), n_folds=4)
# p=np.zeros_like(y)
# for train, test in kf:
####    lr.fit(X[train], y[train])
# p[test]=lr.predict(X[test])
# print(lr.predict(X))
# plt.figure(1)
####plt.scatter(X, y, label='Original')
####plt.scatter(p, y, label='Linear Fit')
####plt.title('Labor Capital Intensity & Labor Productivity, 1899--1922')
####plt.xlabel('Labor Capital Intensity')
####plt.ylabel('Labor Productivity')
# plt.legend()
# plt.grid()
# plt.show()
# =============================================================================
# Cross Validation: Here
# =============================================================================