# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# %% [markdown]
# # **Time Series - Apple Stock**

# %% [markdown]
# **Install the dependencies**

# %%
# !curl -sSL https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt

# %%
# Run this command in terminal before running this notebook as .py script
# Installs dependencies from requirements.txt present in the repo
# %%capture
# !pip install -r https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt

# %% [markdown]
# **Import the libraries**

# %%
import pandas as pd
import matplotlib.pyplot as plt
import os
import env_setup

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Time-Series-Apple-Stock')

# %% [markdown]
# **Read the data**

# %%
apple=pd.read_csv(os.path.join(result_path,'appl_1980_2014.csv'))

# %%
apple.head()

# %%
apple.info()

# %% [markdown]
# **Transform the `Date` column as datetime type**

# %%
# Convert dtype of Date column to datetime64
apple['Date']=pd.to_datetime(apple['Date'],format='%Y-%m-%d')

# %%
apple['Date'].dtype

# %% [markdown]
# **Set the `Date` column as index**

# %%
apple=apple.set_index('Date',drop=True)

# %%
apple

# %% [markdown]
# **Is there any duplicate dates?**

# %%
# Check for duplicates in index
apple.index.is_unique

# %% [markdown]
# **Sort the index from oldest date to recent dates**

# %%
apple=apple.sort_index()

# %%
apple

# %% [markdown]
# **Get the last business day of each month**

# %%
apple.resample('BME').mean()

# %% [markdown]
# **What is the difference between first day and the oldest?**

# %%
(apple.index.max()-apple.index.min()).days

# %% [markdown]
# **How many months do we have in the data?**

# %%
len(apple.resample('BME').mean())

# %% [markdown]
# **Plot the 'Adj Close' value. Set the size of the figure to 13.5 X 9 inches**

# %%
fig=plt.figure(figsize=(13.5,9))
plt.plot(apple['Adj Close'])
plt.xlabel('Year')
plt.ylabel('Adj Close')
plt.title('Year vs Adj Close')
plt.show()

# %%
