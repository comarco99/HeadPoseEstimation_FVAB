import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.metrics
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Lasso
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import utils


path_input="C:/Users/costa/Desktop/PROGETTO_FRATTALI_HDP/PCA/DataFrameWithPCA2.csv"

def get_Linear_Prediction(dati,dipendente):
    X_train, X_test, y_train, y_test = train_test_split(dati, dipendente, test_size=0.3, random_state=0)

    #fit regressione lineare multipla sul train set
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    #predizione del set di test
    y_pred = regressor.predict(X_test)

    # calcoliamo l'errore assoluto medio
    errore = mean_absolute_error(y_test, y_pred)
    print("MAE:", errore)

    return y_test, y_pred, errore

def get_Bayesan_Prediction(dati,dipendente):
    etichette_train, etichette_test = train_test_split(etichette, test_size=0.3, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(dati, dipendente, test_size=0.3, random_state=0)

    #fit regressione lineare multipla sul train set
    regressor = BayesianRidge()
    regressor.fit(X_train, y_train)

    #predizione del set di test
    y_pred = regressor.predict(X_test)

    #calcoliamo l'errore assoluto medio
    errore = mean_absolute_error(y_test, y_pred)
    print("MAE:", errore)

    return y_test,y_pred, errore

def get_Lasso_Prediction(dati,dipendente):
    etichette_train, etichette_test = train_test_split(etichette, test_size=0.3, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(dati, dipendente, test_size=0.3, random_state=0)

    #fit regressione lineare multipla sul train set
    regressor = Lasso(alpha=0.0001, max_iter=100000)
    regressor.fit(X_train, y_train)

    #predizione del set di test
    y_pred = regressor.predict(X_test)

    #calcoliamo l'errore assoluto medio
    errore = mean_absolute_error(y_test, y_pred)
    print("MAE lasso:", errore)

    return y_test, y_pred, errore

def get_GradientBoost_Prediction(dati,dipendente):
    etichette_train, etichette_test = train_test_split(etichette, test_size=0.3, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(dati, dipendente, test_size=0.3, random_state=0)

    #fit regressione lineare multipla sul train set
    regressor = GradientBoostingRegressor()
    regressor.fit(X_train, y_train)

    #predizione del set di test
    y_pred = regressor.predict(X_test)

    #calcoliamo l'errore assoluto medio
    errore = mean_absolute_error(y_test, y_pred)
    print("MAE:", errore)

    return y_test, y_pred, errore

def get_XGBoost_Prediction(dati,dipendente):
    etichette_train, etichette_test = train_test_split(etichette, test_size=0.3, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(dati, dipendente, test_size=0.3, random_state=0)

    #fit regressione lineare multipla sul train set
    regressor = xgb.XGBRegressor()
    regressor.fit(X_train, y_train)

    #predizione del set di test
    y_pred = regressor.predict(X_test)

    #calcoliamo l'errore assoluto medio
    errore = mean_absolute_error(y_test, y_pred)
    print("MAE:", errore)

    return y_test, y_pred, errore

if __name__=='__main__':
#caricamento dei dati
    df = pd.read_csv(path_input, low_memory=False)

    print("DATAFRAME TOTALE\n",df.head())

    #elimino le colonne che non servono in modo da avere un dataframe contenente solo i vettorii
    vettori=df.iloc[:,5:]

    etichette=df.iloc[:,1]#prendo gli id
    #print("etichette\n",etichette)

    pitch=df.iloc[:,2]
    #print("PITCH\n",pitch)
    yaw=df.iloc[:,3]
    #print("YAW\n",yaw)
    roll=df.iloc[:,4]
    #print("ROLL\n",roll )

    print(len(pitch))
    c=0
    for riga in range(len(etichette)):
        if(not(-40<=pitch.loc[riga]<=40 and -40<=yaw.loc[riga]<=40 and -40<=roll.loc[riga]<=40)):
            pitch.drop(riga, inplace=True)
            yaw.drop(riga, inplace=True)
            roll.drop(riga, inplace=True)
            vettori.drop(riga, inplace=True)
            c+=1


    print(c)
    print(len(pitch))


    #**********************************************************************
    print("***************LINEAR REGRESSION********************")

    #regressione pitch
    print("Pitch error linear regression:")
    test1, predizioni1, errore1 =get_Linear_Prediction(vettori, pitch)

    #regressione yaw
    print("Yaw error linear regression:")
    test2, predizioni2, errore2 = get_Linear_Prediction(vettori, yaw)

    #regressione roll
    print("Roll error linear regression:")
    test3, predizioni3, errore3 = get_Linear_Prediction(vettori, roll)

    #**********************************************************************
    print("***************BAYESAN REGRESSION********************")

    # regressione pitch
    print("Pitch error bayesan regression:")
    test1, predizioni1, errore = get_Bayesan_Prediction(vettori, pitch)

    # regressione yaw
    print("Yaw error bayesan regression:")
    test2, predizioni2, errore = get_Bayesan_Prediction(vettori, yaw)

    # regressione roll
    print("Roll error bayesan regression:")
    test3, predizioni3, errore = get_Bayesan_Prediction(vettori, roll)


    # **********************************************************************
    print("***************LASSO REGRESSION********************")

    # regressione pitch
    print("Pitch error lasso regression:")
    test1, predizioni1, errore = get_Lasso_Prediction(vettori, pitch)

    # regressione yaw
    print("Yaw error lasso regression:")
    test2, predizioni2, errore = get_Lasso_Prediction(vettori, yaw)

    # regressione roll
    print("Roll error lasso regression:")
    test3, predizioni3, errore = get_Lasso_Prediction(vettori, roll)


    # **********************************************************************
    print("***************XGB REGRESSION********************")

    # regressione pitch
    print("Pitch error gradient xgb regression:")
    test1, predizioni1, errore = get_XGBoost_Prediction(vettori, pitch)

    # regressione yaw
    print("Yaw error gradient xgb regression:")
    test2, predizioni2, errore = get_XGBoost_Prediction(vettori, yaw)

    # regressione roll
    print("Roll error gradient xgb regression:")
    test3, predizioni3, errore = get_XGBoost_Prediction(vettori, roll)


    # **********************************************************************
    print("***************GRADIENT BOOST REGRESSION********************")

    # regressione pitch
    print("Pitch error gradient boost regression:")
    test1, predizioni1, errore = get_GradientBoost_Prediction(vettori, pitch)

    # regressione yaw
    print("Yaw error gradient boost regression:")
    test2, predizioni2, errore = get_GradientBoost_Prediction(vettori, yaw)

    #regressione roll
    print("Roll error gradient boost regression:")
    test3, predizioni3, errore = get_GradientBoost_Prediction(vettori, roll)

