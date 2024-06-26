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
# # **Grouping - Regiment**

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
# Setup Environment(Downloading data and setting outputs specified in config.yaml)
results_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Grouping-Regiment')

# %% [markdown]
# **Read the data**

# %%
raw_data={'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# %%
regiment=pd.DataFrame(raw_data,columns=['regiment','company','name','preTestScore','postTestScore'])

# %%
regiment.head()

# %%
regiment.info()

# %% [markdown]
# **What is the mean `preTestScore` from the `regiment` Nighthawks**

# %%
regiment.loc[regiment['regiment']=='Nighthawks','preTestScore'].mean()

# %% [markdown]
# **Present general statistics by `company`**

# %%
regiment['company'].describe()

# %% [markdown]
# **What is the mean of each `company's` `preTestScore`?**

# %%
regiment.groupby('company')['preTestScore'].agg('mean')

# %% [markdown]
# **Present the mean `preTestScores` grouped by `regiment` and `company`**

# %%
regiment.groupby(['regiment','company'])['preTestScore'].agg('mean')

# %% [markdown]
# **Present the mean `preTestScores` grouped by `regiment` and `company` without hierarchial indexing**

# %%
regiment.groupby(['regiment','company'])['preTestScore'].agg('mean').unstack()

# %% [markdown]
# **Group the entire dataframe by `regiment` and `company`**

# %%
regiment.groupby(['regiment','company'])[['preTestScore','postTestScore']].mean()

# %% [markdown]
# **What is the number of observations in each `regiment` and `company`?**

# %%
regiment.groupby(['regiment','company'])['name'].count()

# %% [markdown]
# **Iterate over a group and print the `name` and the whole whole data from the regiment**

# %%
for name,group in regiment.groupby('regiment'):
    print(name)
    print(group)

# %%
