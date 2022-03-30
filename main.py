
from functions import (import_clean_data, feature_engineering,
                       label_encode_variable, make_val_split, evaluate_rdmf)

if __name__ == "__main__":
    training_data, test_data = import_clean_data()

    mean_age = round(training_data['Age'].mean())
    training_data = feature_engineering(training_data, mean_age)
    test_data = feature_engineering(test_data, mean_age)

    training_data = label_encode_variable(training_data, "Sex")
    training_data = label_encode_variable(training_data, "Title")
    training_data = label_encode_variable(training_data, "Embarked")

    X_train, X_test, y_train, y_test = make_val_split(training_data)

    evaluate_rdmf(X_train, X_test, y_train, y_test, n_estimators=20)
