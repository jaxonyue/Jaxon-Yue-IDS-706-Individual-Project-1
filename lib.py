import numpy as np
import pandas as pd
import pytest

# Read the uploaded csv file
df = pd.read_csv("train.csv")

# Calculate the mean of fare
mean = np.mean(df['Fare'])
mean

# Calculate the median of fare
median = np.median(df['Fare'])
median

# Calculate the standard deviation of fare
std = np.std(df['Fare'])
std

!pip install pytest nbval
!pytest --nbval "Individual Project 1.ipynb"
