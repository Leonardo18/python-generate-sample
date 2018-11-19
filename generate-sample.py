import pandas as pd
import numpy as np


# read data set from csv
base = pd.read_csv('iris.csv')

# Sample with 0 and 1 and in second parameter the number of 150 registers
# Replace parameter is about reposition, because if set false will generate a sample with one 0 and one 1 and not have enough to make reposition, because all options was used
# In the last parameter a vector for probability of 0.5 for 0.5 given same chance to 0 and 1 to be included
np.random.seed(2345)
sample = np.random.choice(a=[0, 1], size=150, replace=True, p=[0.5, 0.5])


print(sample)
# Exit how many values with zero
print(len(sample[sample == 0]))
# Exit how many values with one
print(len(sample[sample == 1]))
