def replace_NaN_age(dataframe):
	import numpy as np
	mean_age = dataframe["Age"].mean()
	std_dev_age = dataframe["Age"].std()
	
	for index, passenger in dataframe.iterrows():
		if np.isnan(passenger["Age"]): 
			#generate random age with the given std_deviation
			new_age = np.random.normal(loc=mean_age, scale=std_dev_age, size=1)[0]
			if new_age < 0:
				new_age *= -1
				
			dataframe.at[index,"Age"] = new_age