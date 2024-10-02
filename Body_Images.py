import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

from pprint import pprint
import pandas as pd

# Load the .mat files
p1_data = loadmat('data/p1.mat')
t1_data = loadmat('data/t1.mat')
e1_data = loadmat('data/e1.mat')

# Extract p1, t1, and e1 from the loaded data
p1 = p1_data['p1']  # Node coordinates
t1 = t1_data['t1']  # Triangular elements (simplices)
e1 = e1_data['e1']  # Edge elements (if needed for your plot)

# Load sigTrue1 from sig_data.mat
sig_data = loadmat('data/sig_data.mat')
results_df = pd.DataFrame()
for i in range(0, len(sig_data['sig_data'])):
    sigTrue1 = sig_data['sig_data'][i, :]  # Extract the first set of sigTrue1 (or another index)

    # convert to a dataframe to do operations on, such as storing these inside of a dataset
    df = pd.DataFrame(sigTrue1)
    print(df)
    results_df = pd.concat([results_df, df], axis=1)
    

results_df.to_csv("test2.csv", index=False,)



