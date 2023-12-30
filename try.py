import numpy as np
import pandas as pd

dictionary = {
    "nombres":["Johann", "Rene", "Felix"],
    "edad":np.array([15,16,17]),
    "peso":(78, 56, 42),
    "estatura":[1.69, 1.73, 1.75],
    "hermanos":1,
    "genero":"M"
}
df = pd.DataFrame(dictionary)
print(df)