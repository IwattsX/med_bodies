from scipy.io import loadmat

from pprint import pprint
import pandas as pd


# Load sigTrue1 from voltage_data.mat
voltage_data = loadmat('voltage_data.mat')
results_df = pd.DataFrame()
for i in range(0, len(voltage_data['voltage_data'])):
    voltage_data1 = voltage_data['voltage_data'][i, :]  # Extract the first set of voltage_data1 (or another index)

    # convert to a dataframe to do operations on, such as storing these inside of a dataset
    df = pd.DataFrame(voltage_data1)
    print(df)
    results_df = pd.concat([results_df, df], axis=1)
    

results_df.to_csv("dataset/voltageDataset.csv", index=False,)