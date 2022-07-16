import pandas as pd
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
import numpy as np

path_input=""


if __name__=='__main__':
    #caricamento dei dati
    df = pd.read_csv(path_input, low_memory=False)

    #elimino le colonne che non servono in modo da avere un dataframe contenente solo i vettori sui quali effettuare l'analisi
    vettori=df.iloc[:,5:]#elimino le colonne di id, pitch, yaw e roll

    #sostiuisco i valori nan con 0
    vettori=vettori.fillna(0)

    #prima di eseguire l'analisi dei fattori, è necessario valutare la "fattorizzabilità" del nostro set di dati
    #primo metodo: test di Bartlett
    chi_square_value, p_value = calculate_bartlett_sphericity(vettori)
    print(chi_square_value, p_value)

    #secondo metodo: test di Kaiser-Meyer-Olkin
    kmo_all, kmo_model = calculate_kmo(vettori)
    print(kmo_model)


    # CRITERIO DI KAISER
    # Crea l'oggetto dell'analisi dei fattori ed esegui l'analisi dei fattori
    fa = FactorAnalyzer()
    fa.fit(vettori, 25)
    # Controlla gli autovalori
    ev, v = fa.get_eigenvalues()
    print(ev)

    #salvo autovalori in un file
    np.savetxt('C:/Users/costa/Desktop/PROGETTO_FRATTALI_HDP/QuadTree_TotalMatrix/eigenvalues.csv', np.array(ev), delimiter=",")

    # Crea l'oggetto dell'analisi dei fattori ed esegui l'analisi dei fattori
    fa = FactorAnalyzer(600, rotation="varimax")
    fa.fit(vettori, 600)
    fa.loadings_

    varianza_fattori=fa.get_factor_variance()
    print(varianza_fattori)

    #salvo varianza dei 600 fattori in un file
    np.savetxt('C:/Users/costa/Desktop/PROGETTO_FRATTALI_HDP/QuadTree_TotalMatrix/varianze.csv', np.array(varianza_fattori),delimiter=",")


    # SCREE-PLOT
    # Creare uno scree plot usando matplotlib
    plt.scatter(range(1, vettori.shape[1] + 1), ev)
    plt.plot(range(1, vettori.shape[1] + 1), ev)
    plt.title('Scree Plot')
    plt.xlabel('Factors')
    plt.ylabel('Eigenvalue')
    plt.grid()
    plt.show()

