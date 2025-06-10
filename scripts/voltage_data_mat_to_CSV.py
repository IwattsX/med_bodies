import argparse
from scipy.io import loadmat
import pandas as pd

parser = argparse.ArgumentParser(
    prog=__name__,
    description='Converts an matlab mat file to a csv'
)

parser.add_argument("--input", required=True, help="The input data for voltage data")
parser.add_argument("--output", default="./dataset/voltageDataset.csv", help="The output data that will output it as a csv")

args = parser.parse_args()

file_input = args.input
file_output = args.output

# Load sigTrue1 from voltage_data.mat
voltage_data = loadmat(file_input)
results_df = pd.DataFrame()
for i in range(0, len(voltage_data['voltage_data'])):
    voltage_data1 = voltage_data['voltage_data'][i, :]  # Extract the first set of voltage_data1 (or another index)

    # convert to a dataframe to do operations on, such as storing these inside of a dataset
    df = pd.DataFrame(voltage_data1)
    results_df = pd.concat([results_df, df], axis=1)

results_df.to_csv(file_output, index=False,)