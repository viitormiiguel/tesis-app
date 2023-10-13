

import cv2
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler, normalize
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
from sklearn.preprocessing import StandardScaler,  normalize
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import kurtosis, skew, normaltest, jarque_bera
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

# Função para subtrair duas listas
def subtract_lists(list1, list2):

    return [item for item in list1 if item not in list2]

def carrega_dado(path_dado):

    return pd.read_csv(path_dado)

def standardscaler(df_X):
    
    # padronizando variáveis numéricas
    scaler = StandardScaler()
    
    # dependent_cols = df_X.drop('quality', axis = 1).columns
    dependent_cols = df_X.columns
    numerical_data = df_X[dependent_cols].copy()
    
    transformed_x = scaler.fit_transform(numerical_data)
    df_X.loc[:, dependent_cols] = transformed_x
    
    return df_X

def transformadalogaritmica(df_X):
    
    # transformada logaritmica
    coluna_x = df_X.columns.tolist()
    
    for c in coluna_x:
        df_X[c] = np.log(df_X[c]+1)        
    
    df_X = df_X.fillna(0)
    
    return df_X   

def interaction_polynomial(degree):
    
    interaction = PolynomialFeatures(degree=degree, include_bias=False, interaction_only=False)
    
    return interaction

def manipula_dados(df, standard='y',logaritm='y', normalized='y'):
    
    df = df.fillna(0)
    
    if standard in ('y','Y'):
        df = standardscaler(df)
    
    if logaritm in ('y','Y'):
        df = transformadalogaritmica(df)  
        #df = df.fillna(0)    
    
    if normalized in ('y','Y'):
        col = df.columns.tolist()
        df = normalize(df)
        #df = df.fillna(0)
        df = pd.DataFrame(df,columns=col)
    
    return df #df.fillna(0)

def interpretabilidade_lime(path_model, path_treino, path_valida):

    # Parametros no nome do arquivo path_model
    tipo_modelo         = path_model.split('_')[1]
    f                   = path_model.split('feature_')[-1].split('_poly')[0]
    standard            = path_model[path_model.find('standard') + 9]
    logaritm            = path_model[path_model.find('logaritm') + 9]
    normalized          = path_model[path_model.find('normalized') + 11]
    pca                 = path_model[path_model.find('pca') + 4]
    degree              = int(path_model[path_model.find('poly') + 5])

    # Carrega modelo
    arquivo_modelo = jb.load(path_model)
    modelo = arquivo_modelo['modelo']

    # Carrega dataset treino e validacao
    raw = carrega_dado(path_treino)
    raw_val = carrega_dado(path_valida)

    x_treino = raw.copy()
    # x_treino.drop(columns={'Unnamed: 0','Unnamed: 0.1'}, inplace=True)

    x_valida = raw_val.copy()
    # x_valida.drop(columns={'Unnamed: 0','Unnamed: 0.1'}, inplace=True)

    coluna_base = ['path_image']
    coluna_base_feat = ['hu0', 'hu1', 'hu2', 'hu3', 'hu4', 'hu5', 'hu6']

    if f == 'hu_face_toda':
        coluna_base_feature = coluna_base_feat
    if f == 'hu_partes':
        coluna_base_feature = subtract_lists(subtract_lists(x_treino.columns.tolist(), coluna_base), coluna_base_feat)
    if f == 'hu_face_toda_partes':
        coluna_base_feature = subtract_lists(x_treino.columns.tolist(), coluna_base)

    ## manipula dados
    x_treino_temp = manipula_dados(x_treino[coluna_base_feature].copy(), standard,logaritm, normalized)    
    x_valida_temp = manipula_dados(x_valida[coluna_base_feature].copy(), standard,logaritm, normalized)
    
    ## degree
    interaction = interaction_polynomial(degree)   
    x_var       = x_treino_temp.columns.tolist()

    ## traning
    x_treino_temp_inter = pd.DataFrame(interaction.fit_transform(x_treino_temp), columns=interaction.get_feature_names_out(input_features=x_var))
    x_treino_merge      = pd.merge(x_treino[coluna_base], x_treino_temp_inter, left_index=True, right_index=True)

    ## validation
    x_valida_temp_inter = pd.DataFrame(interaction.fit_transform(x_valida_temp), columns=interaction.get_feature_names_out(input_features=x_var))
    x_valida_merge      = pd.merge(x_valida[coluna_base], x_valida_temp_inter, left_index=True, right_index=True)
    
    # busca as features envolvidas conforme modelo  
    try:
        features = modelo.params.index.tolist()        
    except:
        features = modelo.feature_names_in_
        
    ## Lime
    explainer = lime_tabular.LimeTabularExplainer(
        x_treino_merge[features].values, 
        mode="regression", 
        # training_labels=x_treino_merge['comfort'].values, 
        feature_names=features, 
        verbose=True
    )

    for i in range(len(x_valida)): 
        
        if '\\' in x_valida_merge['path_image'][i]:
            frame = x_valida_merge['path_image'][i].split('\\')[-1].split('.')[0]
        else:
            frame = x_valida_merge['path_image'][i].split('/')[-1].split('.')[0]
        
        path_show_in_notebook = path_lime+'lime_explanation_'+tipo_modelo+'_'+frame+'.html'
        explanation = explainer.explain_instance(x_valida_merge[features].values[i], modelo.predict)
        
        # predict_proba=True
        # Salve a saída em um arquivo HTML
        # explanation.show_in_notebook(open_browser=False, notebook_url=None, port=None, host=None, out_file=path_show_in_notebook)
        explanation.save_to_file(path_show_in_notebook)

if __name__ == '__main__':

    path_model = './model/lib/model_statsmodels_feature_hu_face_toda_poly_2_standard_n_logaritm_y_normalized_n_pca_n_.lib'
    path_lime = './model/uv6/lime/'

    path_treino = './model/data/cropped_face_and_parts_frontal_1990f_hu_moments.csv'
    path_valida = './model/images/test/test_4322f_hu_moments.csv'

    # Interpretabilidade LIME
    interpretabilidade_lime(path_model, path_treino, path_valida)
