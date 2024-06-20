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
names = ['Tom','Kris', 'Ahmad', 'Beau']
certificates_earned1.index = names
longest_streak = pd.Series([13,11,9,7], index = names)

certificates_earned1['longest_streak'] = longest_streak ##Adding column longest streak
print(certificates_earned1)

#pandas is cool 

#make a column called certificates per streak 

cond = round((certificates_earned1["Certificates"])/(certificates_earned1['longest_streak']),2) # certificates/ longest streak
certificates_earned1["Cert per Streak"]= cond 
print(certificates_earned1)