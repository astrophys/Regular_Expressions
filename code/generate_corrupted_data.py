# Author : Ali Snedden
# License: MIT
# Date  : 10/17/19
# Purpose: 
#   To generate data that is corrupted to demonstrate vim's powerful regex search and replace
#   functionality.
#   
#
#   File becomes corrupted due to formatting in fout.write() when values are <0 b/c of extra
#   '-' sign
#
#   To Run
#       python code/generate_corrupted_data.py
#
#   Solution to fix corrupted data (in vim)
#       :%s/\([0-9]\.[0-9]\{3\}e[+-][0-9]\{2\}\)\([0-9]\.[0-9]\{3\}e[+-]\)/\1 \2/gc
#
#

import numpy as np
np.random.seed(42)

N=1000
mu1 = 1.95  # mean
s1  = 1     # sigma
mu2 = 4     # mean
s2 = 2      # sigma
mu3 = 100   # mean
s3  = 50    # sigma


value1L = np.random.normal(loc=mu1, scale=s1, size=N)
value2L = np.random.normal(loc=mu2, scale=s2, size=N)
value3L = np.random.normal(loc=mu3, scale=s3, size=N)

fout = open('data/corrupted.txt', 'w+')
for v1,v2,v3 in zip(value1L,value2L,value3L):
    fout.write("{:<10.3e}{:<10.3e}{:<10.3e}\n".format(v1,v2,v3))
fout.close()


