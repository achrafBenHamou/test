"""
Joint à ce script se trouve un jeu de données nommé signal.npy.
Le but de cet exercice est d'extraire des informations de ce signal.


Pour info:
    Les données proviennent d'un drone allant à 7 km / h à une hauteur de 2 mètres du sol 
    et survolant un pipeline de façon longitudinal transportant du gaz.
    Un courant alternatif à été injecté entre ce pipeline et un piquet de terre.
    Un capteur à enregistré la norme du signal magnétique de ce survol.
"""

import os
import numpy
import scipy.fft, scipy.signal
import matplotlib.pyplot as plt

import numpy
def open_file(filename: str):
    """
    Etape 1: Chargement des données numpy
    
    Input: String du nom du fichier
    Output: 1-D array numpy de flottants
    """
    return (numpy.load(filename))
    

class signal_tools:
    def __init__(self):
        """
        Données d entrée:
        acquisition_frequency: Fréquence d'acquisition du convertisseur analogique numérique
        """
        self.__acquisition_frequency = 1991.265812329471  # Hz

    def compute_timestamp(self, signal_data):
        """
        Etape 2: Création d'une liste de temps (abcisse des données)
        
        Création du timestamp à partir du nombre de données et de la fréquence d'acquisition
        """

    @staticmethod
    def compute_fourrier_transform(signal_data, ts):
        """
        Etape 3: Créer le spectre de Fourrier du signal des fréquences comprises entre 1 et 1000 Hz
        
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.fft.html
        
        Inputs:
            signal_data: Les données brutes du fichier signal.npy (Etape 1)
            ts: timestamp du signal (Etape 2)
        """
        import scipy.fft

    @staticmethod
    def get_signal_freq(xf, yf):
        """
        Etape 4: Récupérer de façon automatique la fréquence >= 10 Hz dominante de la transformée de Fourrier (La méthode la plus rapide en temps de calcul est à privilégier)
        
        Le résultat doit être un entier.
        
        Inputs:
            xf: Abscisse du spectre de fourrier
            yf: Ordonnée du spectre de fourrier
        """

    def signal_filtering_func(self, fs, filter_type):
        """
        Etape 5.1: Filtrer les données avec un filtre passe-bas
        
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
        
        Inputs:
            fs: La ou les fréquences critiques. Pour les filtres passe-bas et passe-haut, Wn est un scalaire; 
                pour les filtres passe-bande et coupe-bande, Wn est une séquence de longueur 2. 
                Pour un filtre Butterworth, c'est le point auquel le gain tombe à 1 / sqrt (2) celui de la bande passante (le «point -3 dB»).
                Pour les filtres numériques, Wn est dans les mêmes unités que fs. Par défaut, fs est égal à 2 demi-cycles / échantillon, ils sont donc normalisés de 0 à 1, où 1 est la fréquence de Nyquist. (Wn est donc en demi-cycles / échantillon.)Pour les filtres analogiques, Wn est une fréquence angulaire (par exemple rad / s).
            filter_type: Le type de filtre: {‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}
        """

    @staticmethod
    def low_pass(signal_data):
        """
        Etape 5.2: Filtrer les données avec un filtre passe-bas
        
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html
        La machine capturant les données se déplace à 12 km/h.
        Les anomalies mesurés ont une dimension moyenne de 1 m.
        
        Inputs:
            signal_data: Les données brutes du fichier signal.npy (Etape 1)
        """

    @staticmethod
    def band_pass(signal_data, f1, f2):
        """
        Etape 6: Filtrer les données avec un passe-bande
        
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html
        
        Vous devrez choisir f1 et f2 pour obtenir un bon signal.
        Le pytest de cette fonction défini un "bon signal"
        La moyenne de f1 et f2 doit etre le résultat de l'étape 4
        
        Inputs:
            signal_data: Les données brutes du fichier signal.npy (Etape 1)
            f1: Fréquence minimale
            f1: Fréquence maximale
        """


    @staticmethod
    def get_signal_envelope(signal_data):
        """
        Etape 7: Création de l'enveloppe des données filtrées
        
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html
        
        Tracé de l'enveloppe du signal par la transformée de Hilbert
        
        Inputs:
            signal_data: Les données filtrées passe bande (Etape 6)
        """
        
    @staticmethod
    def plot_all(ts, signal_data, xf, yf, filteredlow_signal, filtered_signal, signal_envelop):
        """
        Etape 8: Affichage de l'ensemble des graphs dans une seule fenêtre avec 3 graphs: (Titre, nom des axes, label, marqueurs)
            1: Données brutes +  Données filtrées passe bas
            2: Fourrier (semilog sur axe Y)
            3: Données filtrées passe bande + enveloppe
        
        Inputs:
            ts: timestamp du signal (Etape 2)
            signal_data: Les données brutes du fichier signal.npy (Etape 1)
            xf: Abscisse du spectre de fourrier
            yf: Ordonnée du spectre de fourrier
            filteredlow_signal: Les données filtrées passe bas (Etape 5.2)
            filtered_signal: Les données filtrées passe bande (Etape 6)
            signal_envelop: Enveloppe des données filtrées pass bande (Etape 7)
        """
        

    @staticmethod
    def remove_side_effect(signal_data, f1, f2):
        """
        Etape 9 bonus: Ne pas avoir d'effets de bord sur l'enveloppe
        
        Atténuation de 9 fois cet effet sur les 1000 premier points et derniers points.
        
        Pistes et explication à rajouter ci dessous:
            ...
        
        Inputs:
            signal_data: Les données brutes du fichier signal.npy (Etape 1)
            f1: Fréquence minimale
            f1: Fréquence maximale
        """


if __name__ == "__main__":
    # Extraction des données
    signal_data = open_file("signal.npy")
    plt.plot(range(len(signal_data)), signal_data)
    plt.show()

    # Création du timestamp
    ts = signal_tools().compute_timestamp(signal_data)
    # plt.plot(ts, signal_data)
    # plt.show()

    # Compute Fourrier
    xf, yf = signal_tools.compute_fourrier_transform(signal_data, ts)
    # plt.plot(xf, yf)
    # plt.show()

    # Frequnecy gather
    fs = signal_tools.get_signal_freq(xf, yf)
    # print("frequency: " + str(fs))

    # Signal filter low pass
    filteredlow_signal = signal_tools.low_pass(signal_data)
    # plt.plot(ts, filteredlow_signal)
    # plt.show()
    
    # Signal filter band pass
    filtered_signal = signal_tools.band_pass(signal_data, fs - 1, fs + 1)
    # plt.plot(ts, filtered_signal)
    # plt.show()

    # Signal env
    signal_envelop = signal_tools.get_signal_envelope(filtered_signal)
    # plt.plot(ts, signal_envelop)
    # plt.show()

    # Data visualisation
    signal_tools.plot_all(ts, signal_data, xf, yf, filteredlow_signal, filtered_signal, signal_envelop)
    
    # Bonus: Remove side effect
    signal_envelop_without_side_effect = signal_tools.remove_side_effect(
        signal_data, fs - 1, fs + 1
    )
    plt.plot(ts, signal_envelop)
    plt.plot(ts, signal_envelop_without_side_effect)
    plt.show()