import pandas as pd
import os
import csv
import numpy as np

path_quadtree_matrix = "C:/Users/costa/Desktop/PROGETTO_FRATTALI_HDP/QuadTree_Compression_Matrix"
path_total_csv_destination = "C:/Users/costa/Desktop/PROGETTO_FRATTALI_HDP/QuadTree_TotalMatrix"


# metodo che a partire dal nome originale del frame,
# ne effettua il rename concatenando anche l'identità del soggetto
def rename_frame(old_name, identity):
    return identity + old_name


# questo metodo a partire dal nome di un frame di un soggetto, effettua un parsing dell'etichetta
# al fine di restituire valori di pitch, roll e yaw
def get_pitch_roll_yaw(frame_name):

    pitch = ""
    roll = ""
    yaw = ""
    posizioni = []
    s = 0
    for c in frame_name:
        if ((c == '+') or (c == '-')):
            posizioni.append(s)
        if (c == 'p'):
            posizioni.append(s - 1)
        s += 1

    pitch = frame_name[posizioni[0]:posizioni[1]]
    yaw = frame_name[posizioni[1]:posizioni[2]]
    roll = frame_name[posizioni[2]:posizioni[3]]

    return pitch, yaw, roll


def total_csv_creator(path_input, path_output):
    #definizione di una lista che conterrà le varie righe che formeranno il dataframe finale
    array_totale=[]

    for folder in os.listdir(path_input):  #per ogni cartella del path di input
        for item in os.listdir(os.path.join(path_input, folder)): #per ogni frame del soggetto corrente
            print(folder)

            #a partire dai csv risultanti dalla codifica con quadtree per ognuno dei soggetti del dataset
            #riempie un pandas datframe
            df_corrente = pd.read_csv(path_input+"/"+folder+"/"+item, sep=';', header=None)#leggo il file csv creato dall'algoritmo

            #istanzio una lista rappresentante la vettorizzazione del csv corrente
            array_corrente=[]

            # effettuo rename del nome del file per avere la colonna con l'dentità
            id = rename_frame(item, folder)

            #effettuo parsing del nome del file per avere pitch roll e yaw
            pitch, yaw, roll = get_pitch_roll_yaw(item)

            #aggiungo id, pitch, yaw e roll al vettore che rappresenterà la riga del dataframe
            array_corrente.append(id)
            array_corrente.append(pitch)
            array_corrente.append(yaw)
            array_corrente.append(roll)

            #effettuo la vettorizzazione del csv corrente contenuto in df_corrente
            #aggiungo i valori al vettore
            for riga in range(len(df_corrente)):
                for colonna in range(6):
                    array_corrente.append(df_corrente.loc[riga,colonna])
            array_totale.append(np.array(array_corrente))

    #converto il vettore di vettori in un numpy array multidimensionale
    array_finale=np.array(np.array(array_totale))

    #creo il dataframe totale
    df_finale=pd.DataFrame.from_records(array_finale)

    # salvo il dataframe totale nel path di destinazione
    df_finale.to_csv(path_output + "/" + "QuadTreeDatasetCompression" + ".csv")


if __name__ == '__main__':
    #a partire da una cartella contenente i file csv restituiti dall'esecuzione di codifica dei frattali con quadtree
    #viene creato un file csv totale contente per ogni soggetto e per ogni frame .csv i risultati della codifica
    #sottoforma di vettore con i rispettivi valori di pitch yaw e roll
    total_csv_creator(path_quadtree_matrix, path_total_csv_destination)


