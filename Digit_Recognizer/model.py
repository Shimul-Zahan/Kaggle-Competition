import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 

sample_submission_path = "./data/sample_submission.csv"
train_path = "./data/train.csv"
test_path = "./data/test.csv"

data = pd.read_csv(train_path)
print(data.iloc[0])