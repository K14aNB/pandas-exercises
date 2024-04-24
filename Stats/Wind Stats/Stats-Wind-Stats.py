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
# # **Stats - Wind Stats**

# %% [markdown]
# **Check and install dependencies**

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
# Setup environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Stats-Wind-Stats')

# %% [markdown]
# **Read the data**

# %%
data=pd.read_csv(os.path.join(result_path,'wind.data'),sep='\s+')

# %%
data.head()

# %%
data.info()

# %%
