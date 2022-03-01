import os
import pandas as pd

construction_path = "data/raw/construction"
construction_files = [f'{construction_path}/{file}' for file in os.listdir(construction_path)]

# Read in them all
df_0 = pd.read_excel(construction_files[0], 1)
df_0

# See how many different formats there are

# Grab relevant rows/values

# Save as csv
