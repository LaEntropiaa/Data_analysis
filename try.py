import numpy as np
import pandas as pd

palabras1 = ["holas", "claro", "super", "huevo", "canasta"]
palabras2 = ["barco", "viento", "iguana", "agua", "caldos"]

palabras1 = [x for i in palabras1 for x in i]

comp = [a + b for a in [x for i in palabras1 for x in i] for b in [y for j in palabras2 for y in j]]
print(comp)