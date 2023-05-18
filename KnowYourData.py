#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from pandas_profiling import ProfileReport

# Get the data
data = pd.read_csv('pima-indians-diabetes.data.csv', sep=';')

print(data.describe())

# %%
# Histogram plot
data['preg'].hist()

#%%
# Density plot
data['age'].plot(kind='density')

#%%
# Box plot
data.plot(kind='box')

#%%
# Correlation plot
plt.matshow(data.corr())

#%%
# Scatter matrix
data.plot.scatter(x='skin', y='test', c='DarkBlue')


# %%
