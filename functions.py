import pandas as pd ; import numpy as np
import matplotlib.pyplot as plt ; import seaborn as sns
import multiprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import pathlib



from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
import time


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import pathlib
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV

def import_clean_data():
    TrainingData = pd.read_csv('train.csv')
    TestData = pd.read_csv('test.csv')
    return TrainingData, TestData

def creation_variable_titre(df: pd.DataFrame, var: str = "Name"):
  x = df['Name'].str.rsplit(",", n = 1).str[-1]
  x = x.str.split().str[0]
  #On note que Dona est présent dans le jeu de test à prédire mais dans les variables d'apprentissage on règle ca a la mano
  return x

def feature_engineering(df, meanAge):
    df['Title'] = creation_variable_titre(df)
    df['Title'] = df['Title'].replace('Dona.', 'Mrs.')
    #affichage des valeurs distinctes obtenues pour le 1er mot après la , dans les 2 dataset
    df['Age'] = df['Age'].fillna(meanAge)
    df['Ticket_Len'] = df['Ticket'].str.len()
    # On s'y connait pas plus sur fare mais on doit la traiter car le dataset de test a une valeur null même sort que l'age on lui met une moyenne
    df['Fare'] = df['Fare'].fillna(df['Fare'].mean())
    # Le nombre de valeur null étant importante on va ajouter la variable hasCabin 1 ou 0 pour ne retenir que si la personne avait une cabine ou non, la encore en se renseignant peut etre que la numérotation des cabines avaient un sens plus précis.
    df['hasCabin'] = df['Cabin'].notnull().astype(int)
    # il a 2 null value dans Embarked qu'on ajoute à la valeur la plus fréquente S
    df['Embarked'] = df['Embarked'].fillna('S')
    df.drop(
    ['PassengerId', 'Name', 'Ticket', 'Cabin'],
    axis = 1, inplace = True)
    return df

def label_encode_variable(df: pd.DataFrame, var: str = "Sex"):
  encoder = LabelEncoder()
  df[var] = encoder.fit_transform(df[var].values)
  return df

def make_val_split(df):
    y = df["Survived"].values
    X = df.drop("Survived", 1).values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    return X_train, X_test, y_train, y_test

def evaluate_rdmf(X_train, X_test, y_train, y_test, n_estimators=20):
    # Train
    rdmf = RandomForestClassifier(n_estimators=n_estimators)
    rdmf.fit(X_train, y_train)

    # Evaluate
    rdmf_score = rdmf.score(X_test, y_test)
    rdmf_score_tr = rdmf.score(X_train, y_train)
    print("{} % de bonnes réponses sur les données de test pour validation (résultat qu'on attendrait si on soumettait notre prédiction sur le dataset de test.csv)".format(round(rdmf_score*100)))
    from sklearn.metrics import confusion_matrix
    print("matrice de confusion")
    print(confusion_matrix(y_test, rdmf.predict(X_test)))
