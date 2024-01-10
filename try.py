import numpy as np
import pandas as pd
import os

titanic_data = pd.read_csv(r"data_sets\titanic_data.csv")

cabin_data = titanic_data["Cabin"].astype(str)
cabin_data = np.array([cabin[0] for cabin in cabin_data])
titanic_data["Cabin"] = pd.Categorical(cabin_data)

tab = pd.crosstab(index=titanic_data["Survived"], columns=titanic_data["Pclass"], margins=True, normalize="columns")
tab.index = ["died", "survived"]
tab.columns = ["class1", "class2", "class3", "Total"]

print(tab)
