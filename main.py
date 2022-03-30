
from functions import *
import os

if __name__ == "__main__":
    TrainingData, TestData = import_clean_data()

    meanAge=round(TrainingData['Age'].mean())
    TrainingData = feature_engineering(TrainingData, meanAge)
    TestData = feature_engineering(TestData, meanAge)

    TrainingData = label_encode_variable(TrainingData, "Sex")
    TrainingData = label_encode_variable(TrainingData, "Title")
    TrainingData = label_encode_variable(TrainingData, "Embarked")

    X_train, X_test, y_train, y_test = make_val_split(TrainingData)

    evaluate_rdmf(X_train, X_test, y_train, y_test, n_estimators=20)
