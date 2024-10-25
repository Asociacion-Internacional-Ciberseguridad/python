from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

predicciones = clf.predict(X_test)
print(f"Exactitud: {accuracy_score(y_test, predicciones)}")
