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
# # **Filtering and Sorting - Euro12**

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
import pandas as pd
import env_setup
import os

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Filtering-and-Sorting-Euro12')

# %% [markdown]
# **Read the data**

# %%
euro12=pd.read_csv(os.path.join(result_path,'Euro_2012_stats_TEAM.csv'))

# %%
euro12.head()

# %%
euro12.info()

# %% [markdown]
# **Select only `Goals` column**

# %%
euro12['Goals']

# %% [markdown]
# **How many teams participated in Euro 2012**

# %%
euro12['Team'].nunique()

# %% [markdown]
# **Number of columns in the dataset**

# %%
euro12.shape[1]

# %% [markdown]
# **DataFrame `discipline` with columns `Team`, `Yellow Cards` and `Red Cards`**

# %%
discipline=euro12.loc[:,['Team','Yellow Cards','Red Cards']]

# %%
discipline.head()

# %%
discipline.info()

# %% [markdown]
# **Sort teams by `Red Cards` then to `Yellow Cards`**

# %%
discipline.sort_values(by=['Red Cards','Yellow Cards'],ascending=False)

# %% [markdown]
# **Calculate the mean of `Yellow Cards` given per team**

# %%
round(discipline['Yellow Cards'].mean(),0)

# %% [markdown]
# **Filter teams that scored more than 6 goals**

# %%
euro12.loc[euro12['Goals']>6,'Team']

# %% [markdown]
# **Select teams that start with 'G'**

# %%
euro12.loc[euro12['Team'].str.startswith('G'),'Team']

# %% [markdown]
# **Select first 7 columns**

# %%
euro12.iloc[:,:7]

# %% [markdown]
# **Select all columns except last 3**

# %%
euro12.iloc[:,:-3]

# %% [markdown]
# **Present only `Shooting accuracy` from England,Italy and Russia**

# %%
euro12.loc[euro12['Team'].isin(['England','Italy','Russia']),['Team','Shooting Accuracy']]

# %%
