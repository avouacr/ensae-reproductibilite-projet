"""Train and evaluate model."""
from sklearn.ensemble import RandomForestClassifier


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
