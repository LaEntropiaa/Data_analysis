import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

diamond_data = pd.read_csv(r"data_sets\diamonds.csv")
del diamond_data["Unnamed: 0"]
diamond_data["cut"] = diamond_data["cut"].map(
    {"Ideal":5, "Premium":4, "Very Good":3, "Good":2, "Fair":1}
    )
diamond_data["clarity"] = diamond_data["clarity"].map(
    {"IF":8, "VVS1":7, "VVS2":6, "VS1":5, "VS2":4, "SI1":3, "SI2":2, "I1":1}
    )

diamond_data["carat"].plot(kind="density")
plt.show()