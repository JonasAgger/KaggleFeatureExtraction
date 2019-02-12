import pandas as pd
import numpy as np

train = pd.read_csv("train.csv")

#Cleanup age
std_div_age = train["Age"].mean()
print(std_div_age)


for index, passenger in train.iterrows():
	if np.isnan(passenger["Age"]): 
		count += 1
print(count)




input("Press Enter to continue...") #Just to not clear the screen immedialy