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
# # **Getting to know the data - World Food Facts**

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
import os
import env_setup

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
results_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Getting-to-know-the-data-World-Food-Facts')

# %% [markdown]
# **Read the data**

# %%
food = pd.read_csv(os.path.join(results_path,'en.openfoodfacts.org.products.tsv'),sep='\t',low_memory=False)

# %%
food.head()

# %%
food.info()

# %% [markdown]
# **Number of observations**

# %%
food.shape[0]

# %% [markdown]
# **Number of columns in the dataset**

# %%
food.shape[1]

# %% [markdown]
# **Print the columns**

# %%
food.columns

# %% [markdown]
# **Column name of 105th column**

# %%
food.columns[104]

# %% [markdown]
# **Dataset Index**

# %%
food.index

# %% [markdown]
# **Product name of 19th observation**

# %%
food.loc[18,'product_name']

# %%
