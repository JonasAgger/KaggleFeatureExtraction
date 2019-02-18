import pandas as pd
import numpy as np
from Utils import *
titanic_train_data = pd.read_csv("train.csv")

#Cleanup age
#replace_NaN_age(titanic_train_data) # Using Gaussian generated Age
titanic_train_data["Age"].fillna(titanic_train_data["Age"].median(), inplace=True)

#Cleanup Sex
titanic_train_data["Sex"].replace(["male", "female"], [0, 1], inplace=True)


columns_to_drop = ["PassengerId", "Ticket", "Cabin", "Embarked", "Name"]
titanic_train_data.drop(columns_to_drop, axis=1, inplace=True)



print(titanic_train_data.info())

input("Press Enter to continue...") #Just to not clear the screen immedialy