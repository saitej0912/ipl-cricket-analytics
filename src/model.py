from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib
import os

def train_model(X, y):
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model, X_train, X_test, y_train, y_test

def evaluate_model(model, X_train, X_test, y_train, y_test):
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    metrics = {
        "train_accuracy": accuracy_score(y_train, y_train_pred),
        "test_accuracy": accuracy_score(y_test, y_test_pred),
        "precision": precision_score(y_test, y_test_pred, average='weighted', zero_division=0),
        "recall": recall_score(y_test, y_test_pred, average='weighted', zero_division=0),
        "f1_score": f1_score(y_test, y_test_pred, average='weighted', zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, y_test_pred)
    }
    return metrics

def save_model(model, feature_cols, model_path, features_path):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    joblib.dump(feature_cols, features_path)
