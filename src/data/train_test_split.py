"""Functions to split data into train/test."""
from sklearn.model_selection import train_test_split


def make_val_split(df):
    "Create validation split."
    y = df["Survived"].values
    X = df.drop("Survived", 1).values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    return X_train, X_test, y_train, y_test
