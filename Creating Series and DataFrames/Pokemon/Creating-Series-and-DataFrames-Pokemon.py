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
# # **Creating Series and DataFrames - Pokemon**

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
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Creating-Series-and-DataFrames-Pokemon')

# %% [markdown]
# **Read the data**

# %%
pokemon_data={
    'name':['Bulbasaur','Charmander','Squirtle','Caterpie'],
    'type':['grass','fire','water','bug'],
    'hp':[45,39,44,45],
    'evolution':['Ivysaur','Charmelon','Wartortle','Metapod'],
    'pokedex':['yes','no','yes','no']
}

# %%
pokemon=pd.DataFrame(pokemon_data,columns=['name','type','hp','evolution','pokedex'])

# %%
pokemon.head()

# %%
pokemon.info()

# %%
pokemon['place']=['ruby','emerald','sapphire','diamond']

# %%
pokemon
