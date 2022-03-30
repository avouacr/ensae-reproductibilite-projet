"""Module with functions."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def import_clean_data():
    "Import raw data."
    training_data = pd.read_csv('train.csv')
    test_data = pd.read_csv('test.csv')
    return training_data, test_data


def creation_variable_titre(df: pd.DataFrame):
    "Extract title."
    x = df['Name'].str.rsplit(",", n=1).str[-1]
    x = x.str.split().str[0]
    return x


def feature_engineering(df, mean_age):
    "Creation of additional features."
    df['Title'] = creation_variable_titre(df)
    df['Title'] = df['Title'].replace('Dona.', 'Mrs.')
    df['Age'] = df['Age'].fillna(mean_age)
    df['Ticket_Len'] = df['Ticket'].str.len()
    df['Fare'] = df['Fare'].fillna(df['Fare'].mean())
    df['hasCabin'] = df['Cabin'].notnull().astype(int)
    df['Embarked'] = df['Embarked'].fillna('S')
    df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
    return df


def label_encode_variable(df: pd.DataFrame, var: str = "Sex"):
    "Label encode a variable."
    encoder = LabelEncoder()
    df[var] = encoder.fit_transform(df[var].values)
    return df


def make_val_split(df):
    "Create validation split."
    y = df["Survived"].values
    X = df.drop("Survived", 1).values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    return X_train, X_test, y_train, y_test


def evaluate_rdmf(X_train, X_test, y_train, y_test, n_estimators=20):
    "Train and evaluate random forest model."
    # Train
    rdmf = RandomForestClassifier(n_estimators=n_estimators)
    rdmf.fit(X_train, y_train)

    # Evaluate
    rdmf_score = rdmf.score(X_test, y_test)
    print("{} % de bonnes réponses sur les données de test pour validation (résultat qu'on attendrait si on soumettait notre prédiction sur le dataset de test.csv)".format(round(rdmf_score*100)))
    from sklearn.metrics import confusion_matrix
    print("matrice de confusion")
    print(confusion_matrix(y_test, rdmf.predict(X_test)))
