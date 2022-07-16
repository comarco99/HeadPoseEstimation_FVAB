import pandas as pd  #to load the dataframe
from sklearn.preprocessing import StandardScaler  #to standardize the features
from sklearn.decomposition import PCA  #to apply PCA
import numpy as np
from sklearn.preprocessing import MinMaxScaler



path_input="C:/Users/costa/Desktop/PROGETTO_FRATTALI_HDP/QuadTree_TotalMatrix/QuadTreeDatasetCompression.csv"

if __name__=='__main__':
    #caricamento dei dati
    df = pd.read_csv(path_input, low_memory=False)

    #elimino le colonne che non servono in modo da avere un dataframe contenente solo i vettori sui quali effettuare l'analisi
    vettori=df.iloc[:,5:]#elimino le colonne di id, pitch, yaw e roll

    etichette=df.iloc[:,1:5]#prendo la restante parte del dataframe

    #sostiuisco i valori nan con 0
    vettori=vettori.fillna(0)

    #Standardizzare le feature
    scalar = StandardScaler()
    scaled_data = pd.DataFrame(scalar.fit_transform(vettori))#scaling dei dati
    print("SCALED DATA\n", scaled_data)

    #Applichiamo la PCA
    #eseguo PCA su 600 componenti
    pca = PCA(n_components=600)
    pca.fit(scaled_data)
    data_pca = pca.fit_transform(scaled_data)
    data_pca = pd.DataFrame(data_pca)
    print("RISULTATO PCA \n", data_pca)


    #La varianza spiegata dice quanta informazione (varianza) può essere attribuita a ciascuna delle componenti principali.
    varianza=pca.explained_variance_ratio_
    np.savetxt("C:/Users/costa/Desktop/PROGETTO_FRATTALI_HDP/VarianzaRatioPCA.csv",varianza,delimiter=',')

    #print("Varianza\n", varianza)
    print("Somma varianze: ", np.sum(varianza))

    finale=pd.merge(left=etichette, right=data_pca, left_index=True, right_index=True)

    #salvo il dataframe totale nel path di destinazione
    finale.to_csv("C:/Users/costa/Desktop/PROGETTO_FRATTALI_HDP/PCA/DataFrameWithPCA.csv")
    
