import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

path_csv_input=""
path_quadtree_matrix=""

def get_size_vector(path_input):
    df = pd.read_csv(path_input)
    vettori=df.iloc[:,5:]
    dimensioni=[]

    ris=vettori.count(axis=1)
    for riga in range(len(ris)):
        el=ris.loc[riga]
        dimensioni.append(el)


    return np.array(dimensioni)


if __name__=='__main__':
    data=get_size_vector(path_csv_input)

    min_index=np.argmin(data)
    min=data[min_index]
    print("Minimo: ", min)

    max_index = np.argmax(data)
    max = data[max_index]
    print("Massimo: ", max)
    
    media=np.mean(data)
    print("Media: ", media)

    primo_quartile=np.quantile(data, q=0.25)
    mediana=np.quantile(data, q=0.50)
    terzo_quartile=np.quantile(data, q=0.75)
    print("Primo quartile: ", primo_quartile)
    print("Mediana: ", mediana)
    print("Terzo quartile: ", terzo_quartile)


    box_result = plt.boxplot(data, meanline=True)
    plt.title("Analisi della dimensonalità")
    plt.show()
