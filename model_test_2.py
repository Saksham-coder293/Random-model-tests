import pandas as pd
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, recall_score  

X ,y = make_moons(n_samples = 1000, noise = 0.01, random_state = 42)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)


print(f"X shape: {X.shape}, y shape: {y.shape}")
print(f"X_train: {X_train.shape}, X_test: {X_test.shape}")
print(f"y_train: {y_train.shape}, y_test: {y_test.shape}")


svm_class = SVC()
svm_class.fit(X_train,y_train)
y_pred = svm_class.predict(X_test)
print(accuracy_score(y_test,y_pred))