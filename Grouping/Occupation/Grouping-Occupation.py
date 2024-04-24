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
# # **Grouping - Occupation**
#

# %% [markdown]
# **Check and install the dependencies**

# %%
# !curl -sSL "https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt"

# %%
# Run this command from terminal before running this notebook as .py script
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
# Setup Environment(Downloading data and setting outputs specified in config.yaml)
results_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Grouping-Occupation')

# %% [markdown]
# **Read the data**

# %%
users=pd.read_csv(os.path.join(results_path,'u.user'),sep='|')

# %%
users.head()

# %%
users.info()

# %% [markdown]
# **Discover mean `age` per `occupation`**

# %%
users.groupby('occupation')['age'].agg('mean')

# %% [markdown]
# **Discover male ratio per `occupation` and sort it from most to the least**

# %%
users[users['gender']=='M'].groupby('occupation')['gender'].agg('count').sort_values(ascending=False)

# %% [markdown]
# **For each `occupation` find the minimum and maximum `age`**

# %%
users.groupby('occupation')['age'].agg(['min','max'])

# %% [markdown]
# **For each combination of `occupation` and `gender`, calculate the mean `age`**

# %%
users.groupby(['occupation','gender'])['age'].agg('mean')

# %% [markdown]
# **For each occupation present the percentage of men and women**

# %%
users.groupby('occupation')['gender'].value_counts(normalize=False)

# %%
