

import cv2
import numpy as np
import pandas as pd
from sklearn.preprocessing  import  StandardScaler, normalize 
from sklearn.ensemble import GradientBoostingRegressor, HistGradientBoostingRegressor, AdaBoostRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import VotingRegressor
from sklearn.metrics import r2_score

import statsmodels.api as sm
import statsmodels.stats.api as sms
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.compat import lzip
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.gofplots import qqplot
from sklearn.preprocessing  import  StandardScaler,  normalize 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import kurtosis,skew,normaltest,jarque_bera
from scipy import stats

from sklearn.preprocessing import PolynomialFeatures
from lime import lime_tabular
from lime.lime_tabular import LimeTabularExplainer

from sklearn.decomposition import PCA
import sklearn

import joblib as jb
import pickle
import matplotlib.pyplot as plt

import warnings

