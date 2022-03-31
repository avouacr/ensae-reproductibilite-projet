"""Functions to perform feature engineering."""
import pandas as pd
from sklearn.preprocessing import LabelEncoder


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
