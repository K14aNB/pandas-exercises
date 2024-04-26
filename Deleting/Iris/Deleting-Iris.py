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
# # **Deleting - Iris**

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
import numpy as np
import pandas as pd
import os
import env_setup

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Deleting-Iris')

# %% [markdown]
# **Read the data**

# %%
iris=pd.read_csv(os.path.join(result_path,'iris.data'))

# %%
iris.head()

# %%
iris.info()

# %% [markdown]
# **Rename Columns**

# %%
iris=iris.rename(columns={'5.1':'sepal_length (in cm)','3.5':'sepal_width (in cm)','1.4':'petal_length (in cm)','0.2':'petal_width (in cm)','Iris-setosa':'class'})

# %%
iris

# %% [markdown]
# **Is there any missing values in the dataset?**

# %%
iris.isna().sum().sum()>0

# %% [markdown]
# **Set the values of row 10 to 29 of the column `petal_length (in cm)` to NaN**

# %%
iris.loc[10:29,'petal_length (in cm)']=np.NaN

# %%
iris.loc[10:29]

# %% [markdown]
# **Substitute the NaN values to 1.0**

# %%
iris.isna().sum()

# %%
iris=iris.replace(to_replace=np.NaN,value=1)

# %%
iris.loc[10:29]

# %% [markdown]
# **Delete `class` column**

# %%
iris=iris.drop(columns=['class'],axis=1)

# %%
iris.head()

# %% [markdown]
# **Set the first 3 rows as NaN**

# %%
iris.loc[:2]=np.NaN

# %%
iris.head()

# %% [markdown]
# **Delete the empty rows**

# %%
iris=iris.dropna()

# %%
iris.head()

# %% [markdown]
# **Reset the index**

# %%
iris=iris.reset_index(drop=True)

# %%
iris.head()

# %%
