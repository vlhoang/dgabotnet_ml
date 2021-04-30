import pandas as pd
import numpy as np
dataset = pd.read_csv("100000dga_full_features_all.csv")
dataset = dataset.sample(frac=1)
dataset.to_csv("100000dga_full_features_all_mixed.csv")