##Pandas Introduction Practice 

import pandas as pd
import numpy as np
import matplotlib as plt


certificates_earned = pd.Series(
    [8,2,5,6],
    index = ['Tom','Kris','Ahmad','Beau']
)
print(certificates_earned)

certificates_earned1 = pd.DataFrame({
    'Certificates':[8,2,5,6],
    'Time (in months)':[16,5,9,12]
 

})
certificates_earned1.index = ['Tom','Kris', 'Ahmad', 'Beau']
print(certificates_earned1.iloc[2])