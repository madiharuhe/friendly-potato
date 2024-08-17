from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, confusion_matrix

X, Y = load_iris(return_X_Y=True)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

Y_pred = KNeighborsClassifier(5).fit(X_train, Y_train).predict(X_test)

print(confusion_matrix(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred))
