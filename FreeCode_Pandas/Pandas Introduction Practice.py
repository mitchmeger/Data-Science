##Pandas Introduction Practice 

import pandas as pd
import numpy as np
import matplotlib as plt


certificates_earned = pd.Series(
    [8,2,5,6],
    index = ['Tom','Kris','Ahmad','Beau']
)
print(certificates_earned)