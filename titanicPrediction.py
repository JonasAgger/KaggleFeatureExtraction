from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

import pandas as pd
import numpy as np
from Utils import *
titanic_train_data = pd.read_csv("train.csv")
titanic_test_data = pd.read_csv("test.csv")

#Cleanup age
#replace_NaN_age(titanic_train_data) # Using Gaussian generated Age
titanic_train_data["Age"].fillna(titanic_train_data["Age"].median(), inplace=True)
titanic_test_data["Age"].fillna(titanic_train_data["Age"].median(), inplace=True)

#Cleanup Sex
titanic_train_data["Sex"].replace(["male", "female"], [0, 1], inplace=True)
titanic_test_data["Sex"].replace(["male", "female"], [0, 1], inplace=True)


train_columns_to_drop = ["PassengerId", "Ticket", "Cabin", "Embarked", "Name"]
test_columns_to_drop = ["Ticket", "Cabin", "Embarked", "Name"] # need the name here
titanic_train_data.drop(train_columns_to_drop, axis=1, inplace=True)
titanic_test_data.drop(test_columns_to_drop, axis=1, inplace=True)

#add fare to missing fare
titanic_test_data["Fare"].fillna(titanic_train_data["Fare"].mean(), inplace=True)

X_train = titanic_train_data.drop("Survived", axis=1)
Y_train = titanic_train_data["Survived"]
X_test = titanic_test_data.drop("PassengerId", axis=1).copy()


logistic_regression = LogisticRegression()
sgdClassifier = SGDClassifier()
svm = SVC()
random_forest = RandomForestClassifier(n_estimators=100)

logistic_regression.fit(X_train, Y_train)
sgdClassifier.fit(X_train, Y_train)
svm.fit(X_train, Y_train)
random_forest.fit(X_train, Y_train)

print("Printing Scores:")
print("LogisticRegression: ", logistic_regression.score(X_train, Y_train))
print("SGDClassifier: ", sgdClassifier.score(X_train, Y_train))
print("SVM: ", svm.score(X_train, Y_train))
print("RandomForestClassifier: ", random_forest.score(X_train, Y_train))

input("Press Enter to continue...") #Just to not clear the screen immedialy