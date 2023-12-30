import numpy as np
import pandas as pd
data = np.random.uniform(0, 1, 25)

data = np.where(data >= .5, data, 0)

print(data)


