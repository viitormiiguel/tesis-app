
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

warnings.filterwarnings("ignore") # To ignore warnings

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

def carrega_dado(path_dado):
    
    return pd.read_csv(path_dado)

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

def split_dados(X,Y):
    
    X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size = 0.20, random_state = 5)
    
    return X_train, X_test, Y_train, Y_test 


def interaction_polynomial(degree):
    
    interaction = PolynomialFeatures(degree=degree, include_bias=False, interaction_only=False)
    
    return interaction

def remove_p_value_maior_alfa(model, X_inter, Y_inter):
    
    condicao = True
    
    while condicao:    
    
        dt_pvalues = model.pvalues
        dt_pvalues = dt_pvalues.reset_index()
        dt_pvalues.rename(columns={0:'pvalue'}, inplace=True)
        
        indice_max = dt_pvalues['pvalue'].idxmax()
        
        if dt_pvalues['pvalue'][indice_max] > 0.05:
            dt_pvalues = dt_pvalues.drop(indice_max)
            colunas_novas = dt_pvalues['index'].tolist()
            model = model_ols(X_inter[colunas_novas], Y_inter)
        else:
            condicao = False
            
    return model

def model_ols(X, Y):
    
    model = sm.OLS(Y,X).fit()
    model = remove_p_value_maior_alfa(model, X_inter, Y_inter)
    
    return model

def modelo_emsemble_voltingRegressor(X_train, y_train, X_test, y_test):
    
    # Melhores hiperparâmetros encontrados com GridSearchCV para 
    GradientBoostingRegressor_melhores_hiperparametros = {
        'n_estimators': 300,
        'learning_rate': 0.1,
        'max_depth': 5
    }

    XGBRegressor_melhores_hiperparametros = {
        'n_estimators': 300,
        'learning_rate': 0.1,
        'max_depth': 7
    }

    LGBMRegressor_melhores_hiperparametros = {
        'n_estimators': 300,
        'learning_rate': 0.1,
        'max_depth': 7
    }

    # Melhores hiperparâmetros encontrados com GridSearchCV para 
    AdaBoostRegressor_melhores_hiperparametros = {
        'base_estimator__max_depth': 9, 
        'learning_rate': 0.1, 
        'n_estimators': 300
    }

    # Inicializar os modelos
    model1 = GradientBoostingRegressor(**GradientBoostingRegressor_melhores_hiperparametros)
    model2 = XGBRegressor(**XGBRegressor_melhores_hiperparametros)
    model3 = LGBMRegressor(**LGBMRegressor_melhores_hiperparametros)
    model4 = HistGradientBoostingRegressor()
    model5 = AdaBoostRegressor(base_estimator=DecisionTreeRegressor(max_depth=AdaBoostRegressor_melhores_hiperparametros['base_estimator__max_depth']),
                               n_estimators=AdaBoostRegressor_melhores_hiperparametros['n_estimators'],
                               learning_rate=AdaBoostRegressor_melhores_hiperparametros['learning_rate'])

    # Treinar cada modelo
    model1.fit(X_train, y_train)
    model2.fit(X_train, y_train)
    model3.fit(X_train, y_train)
    model4.fit(X_train, y_train)
    model5.fit(X_train, y_train)
    
    # Fazer previsões para o conjunto de teste
    pred1 = model1.predict(X_test)
    pred2 = model2.predict(X_test)
    pred3 = model3.predict(X_test)
    pred4 = model4.predict(X_test)
    pred5 = model5.predict(X_test)

    # Calcular o RMSE para cada modelo individual
    rmse1 = np.sqrt(mean_squared_error(y_test, pred1))
    rmse2 = np.sqrt(mean_squared_error(y_test, pred2))
    rmse3 = np.sqrt(mean_squared_error(y_test, pred3))
    rmse4 = np.sqrt(mean_squared_error(y_test, pred4))
    rmse5 = np.sqrt(mean_squared_error(y_test, pred5))

    # Calcular os pesos inversamente proporcionais aos valores do RMSE
    weights = [1 / rmse for rmse in [rmse1, rmse2, rmse3, rmse4, rmse5]]
    total_weights = sum(weights)
    weights = [weight / total_weights for weight in weights]

    # Criar o VotingRegressor com os pesos definidos pelo RMSE
    voting_model = VotingRegressor([('gb', model1), ('xgb', model2), ('lgb', model3), 
                                    ('hist', model4), ('ada', model5)], 
                                   weights=weights)

    # Treinar o VotingRegressor com o conjunto de treinamento completo
    voting_model.fit(X_train, y_train)
    
    return voting_model

# Função para subtrair duas listas
def subtract_lists(list1, list2):
    
    return [item for item in list1 if item not in list2]    

def salva_modelo(model, path_modelo):
    
    jb.dump(model,path_modelo)
    
def avalia_pca(X):
    
    # Aplicar o PCA
    pca = PCA()
    pca.fit(X)
    
    explained_variance_ratio = pca.explained_variance_ratio_
    cumulative_variance = np.cumsum(explained_variance_ratio)
    
    # Encontrar o número de componentes onde a curva começa a nivelar
    threshold = 0.95  # Por exemplo, 95% de variância explicada
    n_components = np.argmax(cumulative_variance >= threshold) + 1
    
    # Criar uma instância PCA
    pca = PCA(n_components=n_components)    
    pca.fit(X)
    
    # Aplicar o PCA aos dados
    pca_result = pca.fit_transform(X)
    
    # Obter as variáveis (features) e o percentual de importância em cada componente
    feature_names               = X.columns.tolist()
    components                  = pca.components_
    explained_variance_ratio    = pca.explained_variance_ratio_

    # Criar um DataFrame para visualização
    component_data = []

    for i, component in enumerate(components):
        
        sorted_idx = np.argsort(np.abs(component))[::-1]
        sorted_vars = ', '.join([feature_names[idx] for idx in sorted_idx])
        component_data.append({
            'Componente': f'Componente {i+1}',
            'Variáveis': sorted_vars,
            'Percentual de Importância': explained_variance_ratio[i] * 100
        })

    component_df = pd.DataFrame(component_data)
    
    return pca, pca_result, component_df

def pca_fit_transform(modelo, dados):
    
    return  modelo.fit_transform(dados)

def interpretabilidade_lime(path_model, path_treino, path_valida):
    
    # parametros no nome do arquivo path_model
    tipo_modelo = path_model.split('_')[1]
    f           = path_model.split('feature_')[-1].split('_poly')[0]
    standard    = path_model[path_model.find('standard') + 9]
    logaritm    = path_model[path_model.find('logaritm') + 9]
    normalized  = path_model[path_model.find('normalized') + 11]
    pca         = path_model[path_model.find('pca') + 4]
    degree      = int(path_model[path_model.find('poly') + 5])
            
    # carrega modelo
    arquivo_modelo  = jb.load(path_model)
    modelo          = arquivo_modelo['modelo']
        
    # carrega dataset treino e validacao
    raw     = carrega_dado(path_treino)
    raw_val = carrega_dado(path_valida)
        
    x_treino = raw.copy()
    x_treino.drop(columns={'Unnamed: 0','Unnamed: 0.1'}, inplace=True)

    x_valida = raw_val.copy()
    x_valida.drop(columns={'Unnamed: 0','Unnamed: 0.1'}, inplace=True)
    
    coluna_base         = [ 'path_image', 'character', 'comfort', 'UV' ]
    coluna_base_feat    = [ 'hu0', 'hu1', 'hu2', 'hu3', 'hu4', 'hu5', 'hu6' ]
    
    if f == 'hu_face_toda':
        coluna_base_feature = coluna_base_feat
    if f == 'hu_partes':
        coluna_base_feature = subtract_lists(subtract_lists(x_treino.columns.tolist(), coluna_base), coluna_base_feat)
    if f == 'hu_face_toda_partes':
        coluna_base_feature = subtract_lists(x_treino.columns.tolist(), coluna_base)
        
    # manipula dados
    x_treino_temp = manipula_dados(x_treino[coluna_base_feature].copy(), standard,logaritm, normalized)    
    x_valida_temp = manipula_dados(x_valida[coluna_base_feature].copy(), standard,logaritm, normalized)
    
    # degree
    interaction = interaction_polynomial(degree)   
    x_var       = x_treino_temp.columns.tolist()

    # traning
    x_treino_temp_inter = pd.DataFrame(interaction.fit_transform(x_treino_temp), columns=interaction.get_feature_names_out(input_features=x_var))
    x_treino_merge      = pd.merge(x_treino[coluna_base], x_treino_temp_inter, left_index=True, right_index=True)

    # validation
    x_valida_temp_inter = pd.DataFrame(interaction.fit_transform(x_valida_temp), columns=interaction.get_feature_names_out(input_features=x_var))
    x_valida_merge      = pd.merge(x_valida[coluna_base], x_valida_temp_inter, left_index=True, right_index=True)
    
    # busca as features envolvidas conforme modelo  
    try:
        features = modelo.params.index.tolist()        
    except:
        features = modelo.feature_names_in_
            
    # lime
    explainer = lime_tabular.LimeTabularExplainer(x_treino_merge[features].values, mode="regression", training_labels=x_treino_merge['comfort'].values, feature_names=features, verbose=True)
    
    for i in range(len(x_valida)): 
        
        character   = x_valida_merge['character'][i]
        frame       = x_valida_merge['path_image'][i].split('\\')[-1].split('.')[0]
        path_show_in_notebook = path_lime+'lime_explanation_'+tipo_modelo+'_'+str(character)+'_'+frame+'.html'
        explanation = explainer.explain_instance(x_valida_merge[features].values[i], modelo.predict)
        # predict_proba=True
        # Salve a saída em um arquivo HTML
        # explanation.show_in_notebook(open_browser=False, notebook_url=None, port=None, host=None, out_file=path_show_in_notebook)
        explanation.save_to_file(path_show_in_notebook)

def interpretabilidade_PCA(path_model, path_treino):
    
    #f = ['hu_face_toda', 'hu_partes', 'hu_face_toda_partes']
    
    #parametros no nome do arquivo path_model
    tipo_modelo = path_model.split('_')[1]
    f           = path_model.split('feature_')[-1].split('_poly')[0]
    standard    = path_model[path_model.find('standard') + 9]
    logaritm    = path_model[path_model.find('logaritm') + 9]
    normalized  = path_model[path_model.find('normalized') + 11]
    pca         = path_model[path_model.find('pca') + 4]
    pca_name    = path_model[path_model.find('pca') + 4]
    degree      = int(path_model[path_model.find('poly') + 5])
    
    # carrega modelo
    arquivo_modelo = jb.load(path_model)
    modelo = arquivo_modelo['modelo']
    
    #carrega dataset treino e validacao
    raw = carrega_dado(path_treino)
    
    x_treino = raw.copy()
    x_treino.drop(columns={'Unnamed: 0','Unnamed: 0.1'}, inplace=True)
   
    coluna_base = [ 'path_image', 'character', 'comfort', 'UV' ]
    coluna_base_feat = [ 'hu0', 'hu1', 'hu2', 'hu3', 'hu4', 'hu5', 'hu6' ]    
    
    if f == 'hu_face_toda':
        coluna_base_feature = coluna_base_feat
    if f == 'hu_partes':
        coluna_base_feature = subtract_lists(subtract_lists(x_treino.columns.tolist(), coluna_base), coluna_base_feat)
    if f == 'hu_face_toda_partes':
        coluna_base_feature = subtract_lists(x_treino.columns.tolist(), coluna_base)    
    
    if pca_name in ['s','S']:    
        
        modelo_pca = arquivo_modelo['modelo_pca']        
        col_pca = [ 'componente'+str(i) for i in range(1,modelo_pca.n_components_+1) ]        
    
        # manipula dados
        x_treino_temp = manipula_dados(x_treino[coluna_base_feature].copy(), standard,logaritm, normalized)
        x_treino_merge = pd.merge(x_treino[coluna_base], x_treino_temp, left_index=True, right_index=True)           
               
        # Criar uma instância PCA
        pca = PCA(n_components=modelo_pca.n_components)    
        pca.fit(x_treino_merge[coluna_base_feature])
        
        explained_variance_ratio = pca.explained_variance_ratio_
        cumulative_variance = np.cumsum(explained_variance_ratio)
        
        # Aplicar o PCA aos dados
        pca_result = pca.fit_transform(x_treino_merge[coluna_base_feature])
                
        feature_names = col_pca
        
        # Aplique PCA para reduzir a dimensionalidade para 4 componentes (o máximo possível)
        pca = PCA(n_components=modelo_pca.n_components)
        X_pca = pca.fit_transform(x_treino_merge[coluna_base_feature])
    
        # Obtenha o explained_variance_ratio dos componentes principais
        explained_variance_ratio = pca.explained_variance_ratio_
    
        # Obtenha os vetores de carga (loadings) para cada componente
        loadings = pca.components_
    
        # Crie um gráfico de barras não empilhado
        n_components    = len(explained_variance_ratio)
        n_features      = len(feature_names)
        width           = 0.35  # Largura das barras
        x               = np.arange(n_features)  # Posições no eixo x
    
        fig, ax = plt.subplots(figsize=(10, 6))
    
        for i in range(n_components):
            
            loading_contributions = (loadings[i] ** 2) * explained_variance_ratio[i]
            ax.bar(x, loading_contributions, width, label=f'Componente {i+1}')
    
        # Adicione rótulos e legendas
        ax.set_xlabel('Variável')
        ax.set_ylabel('Taxa de Variância Explicada')
        ax.set_title('Taxa de Variância Explicada por Variável em Cada Componente Principal')
        ax.set_xticks(x)
        ax.set_xticklabels(feature_names, rotation=45)
        ax.legend()
        
        # Salve o gráfico em um arquivo de imagem (por exemplo, PNG)
        path_pca_fig = path_lime+'pca_explanation_'+tipo_modelo+'_feature_'+f+'_standard_'+standard+'_logaritm_'+logaritm+'_normalized_'+normalized+'_pca_'+pca_name+'_degree_'+str(degree)+'.png'
        
        plt.savefig(path_pca_fig)
    
        plt.show()        
        
if __name__ == '__main__':
    
    path_model  = './model/lib/model_statsmodels_feature_hu_face_toda_poly_2_standard_n_logaritm_y_normalized_n_pca_n_.lib'
    path_lime   = './model/uv6/lime/'
    
    path_treino = './model/data/cropped_face_and_parts_frontal_1990f_hu_moments.csv'
    path_valida = './model/data/cropped_val_face_frontal_and_parts_4322f_hu_moments.csv'
    
    # Interpretabilidade LIME 
    interpretabilidade_lime(path_model, path_treino, path_valida)
    
    ## ===========================================================================
    
    path_model  = './model/lib/model_statsmodels_feature_hu_partes_poly_2_standard_n_logaritm_n_normalized_y_pca_n_.lib'
    path_lime   = './model/uv6/lime/'
    
    path_treino = './model/data/cropped_face_and_parts_frontal_1990f_hu_moments.csv'
    path_valida = './model/data/cropped_val_face_frontal_and_parts_4322f_hu_moments.csv'
    
    # Interpretabilidade LIME 
    # interpretabilidade_lime(path_model, path_treino, path_valida)