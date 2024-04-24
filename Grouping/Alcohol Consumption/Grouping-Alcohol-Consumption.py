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
# # **Grouping - Alcohol Consumption**

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
# **Import libraries**

# %%
import pandas as pd
import env_setup
import os

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
results_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Grouping-Alcohol-Consumption')

# %% [markdown]
# **Read the data**

# %%
drinks=pd.read_csv(os.path.join(results_path,'drinks.csv'))

# %%
drinks.head()

# %%
drinks.info()

# %% [markdown]
# **Which continent drinks more beer on average?**

# %%
drinks.groupby('continent')['beer_servings'].agg('mean').nlargest(1)

# %% [markdown]
# **For each continent print the statistics for wine consumption**

# %%
drinks.groupby('continent')['wine_servings'].describe()

# %% [markdown]
# **Print the mean alcohol consumption per continent for every column**

# %%
alcohols=['beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol']

# %%
drinks.groupby('continent')[alcohols].agg('mean')

# %% [markdown]
# **Print the median alcohol consumption per continent for every column**

# %%
drinks.groupby('continent')[alcohols].agg('median')

# %% [markdown]
# **Print the mean, min and max values for spirit consumption**

# %%
drinks.groupby('continent')['spirit_servings'].agg(['mean','min','max'])

# %%
