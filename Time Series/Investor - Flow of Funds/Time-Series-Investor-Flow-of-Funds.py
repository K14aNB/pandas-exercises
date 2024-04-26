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
# # **Time Series - Investor Flow of Funds**

# %% [markdown]
# **Check and install the dependencies**

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
import os
import env_setup

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Time-Series-Investor-Flow-of-Funds')

# %% [markdown]
# **Read the data**

# %%
df=pd.read_csv(os.path.join(result_path,'weekly.csv'))

# %%
df.head()

# %%
df.info()

# %% [markdown]
# **What is the frequency of the dataset?**

# %% [markdown]
# **`Weekly data`**

# %% [markdown]
# **Set the `Date` column as index**

# %%
df=df.set_index('Date',drop=True)

# %%
df.head(10)

# %% [markdown]
# **What is the dtype of index?**

# %%
df.index.dtype

# %% [markdown]
# **Set the index to DateTimeIndex type**

# %%
df.index=df.index.astype('datetime64[ns]')

# %%
df.head(10)

# %% [markdown]
# **Change frequency to monthly, sum the values and assign to monthly**

# %%
monthly=df.resample('ME').sum()

# %%
monthly

# %% [markdown]
# **Drop the rows with `Total` as zero**

# %%
monthly=monthly.drop(index=monthly.loc[monthly['Total']==0].index)

# %%
monthly

# %% [markdown]
# **Change frequency to Yearly**

# %%
yearly=monthly.resample('YE').sum()

# %%
yearly

# %%
