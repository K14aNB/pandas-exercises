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
# # **Merge - Housing Market**

# %% [markdown]
# **Check and install the dependencies**

# %%
# !curl -sSL "https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt"

# %%
# Run this command in terminal before running this notebook as .py script
# Installs dependencies from requirements.txt present in the repo
# %%capture
# !pip install -r "https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt"

# %% [markdown]
# **Import the libraries**

# %%
import numpy as np
import pandas as pd
import env_setup
import os

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Merge-Housing-Market')

# %% [markdown]
# **Read the data**

# %%
series_1=pd.Series(np.linspace(1,4,100))
series_2=pd.Series(np.linspace(1,3,100))
series_3=pd.Series(np.linspace(10000,30000,100))

# %% [markdown]
# **Create a dataframe by joining `series_1`, `series_2`, `series_3` by column**

# %%
data=pd.concat([series_1,series_2,series_3],axis=1)

# %%
data.head()

# %%
data.info()

# %% [markdown]
# **Change the name of columns to `bedrs`, `bathrs`, `price_sqr_meter`**

# %%
data=data.rename(columns={0:'bedrs',1:'bathrs',2:'price_sqr_meter'})
data

# %% [markdown]
# **Create one column dataframe with the values of `series_1`, `series_2`, `series_3` and assign it to `bigcolumn`**

# %%
data_1=pd.DataFrame(pd.concat([series_1,series_2,series_3]).reset_index(drop=True)).rename(columns={0:'bigcolumn'})

# %%
data_1

# %%
