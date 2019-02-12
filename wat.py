import pandas as pd
import numpy as np
from Utils import *
train = pd.read_csv("train.csv")

#Cleanup age
replace_NaN_age(train)
print(train.info())

columns_to_drop = ["PassengerId", "Ticket", "Cabin"]
train.drop(columns_to_drop, axis=1, inplace=True)

input("Press Enter to continue...") #Just to not clear the screen immedialy