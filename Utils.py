import numpy as np

def gaussian(mean,std_dev):
  z1 = sqrt(-2*log(mean))*cos(2*pi*std_dev)
  return z1

def replace_NaN_age(dataframe):
	mean_age = dataframe["Age"].mean()
	std_dev_age = dataframe["Age"].std()
	
	for index, passenger in dataframe.iterrows():
		if np.isnan(passenger["Age"]): 
			#generate random age with the given std_deviation
			new_age = gaussian(mean_age, std_dev_age)
			if new_age < 0:
				new_age *= -1
				
			dataframe.at[index,"Age"] = new_age