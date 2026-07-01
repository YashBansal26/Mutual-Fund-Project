import pandas as pd
import os

path = "data/raw"

for file in os.listdir(path):
    if file.endswith(".csv"):
        print("="*60)
        print(file)

        df = pd.read_csv(os.path.join(path, file))

        print("Shape:")
        print(df.shape)

        print("\nDtypes:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())