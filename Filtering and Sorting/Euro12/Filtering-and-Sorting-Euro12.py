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
# **Import the libraries**

# %%
import pandas as pd
import sys
import os
from urllib3 import PoolManager,request

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment
# Github gist url for Python Script which will perform environment setup
env_url='https://gist.githubusercontent.com/K14aNB/46becb626d36ad8fa8d445616241dfef/raw/'
http=PoolManager()
response=http.request('GET',env_url)
if response.status==200:
    exec(response.data.decode('utf-8'))
    setup(repo_path='pandas-exercises',nb_name='Filtering-and-Sorting-Euro12')

# %% [markdown]
# **Read the data**

# %%
if 'google.colab' not in sys.modules:
    dir=os.path.join(os.getcwd(),'Data Science','Git Repos','pandas-exercises')
else:
    dir=os.getcwd()
euro12=pd.read_csv(os.path.join(dir,'data','Euro_2012_stats_TEAM.csv'))

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
