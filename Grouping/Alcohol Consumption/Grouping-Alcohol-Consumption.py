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
# **Import libraries**

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
    setup(repo_path='pandas-exercises',nb_name='Grouping-Alcohol-Consumption')

# %% [markdown]
# **Read the data**

# %%
if 'google.colab' not in sys.modules:
    dir=os.path.join(os.getcwd,'Data Science','Git Repos','pandas-exercises')
else:
    dir=os.getcwd()
drinks=pd.read_csv(os.path.join(dir,'data','drinks.csv'))

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
