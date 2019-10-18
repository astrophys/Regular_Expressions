# Author : Ali Snedden
# License: MIT
# Date  : 10/17/19
# Purpose: 
#   
#   
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_table(filepath_or_buffer="data/fixed.txt", sep=" ")
v1 = df.iloc[:,1].values
v2 = df.iloc[:,2].values
v3 = df.iloc[:,3].values

plt.hist(v1,histtype='bar', ec='black', label='col 1')
plt.hist(v2,histtype='bar', ec='blue', label='col 2')
#plt.hist(v3,histtype='bar', ec='red', label='col 3')
plt.legend(loc='upper right')
plt.show()
