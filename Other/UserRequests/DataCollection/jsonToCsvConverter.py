import pandas as pd
import json

with open('Data/raw_dataset.json') as f:
    data = json.load(f)

df = pd.json_normalize(data)
df.to_csv('Data/raw_dataset.csv', index=False)
