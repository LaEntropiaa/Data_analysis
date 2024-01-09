import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.read_csv(r"data_sets\dates.csv", parse_dates=[0,1,2,3], date_parser= lambda x: pd.to_datetime(x, format="mixed"))

date_set1 = dates.iloc[:,0]
date_set1 = pd.DataFrame({"year":date_set1.dt.year,
                          "month":date_set1.dt.month,
                          "day":date_set1.dt.day,
                          "hour":date_set1.dt.hour,
                          "dayofyear":date_set1.dt.dayofyear,
                          "weekday":date_set1.dt.weekday,
                          "quarter":date_set1.dt.quarter})
print(date_set1)
