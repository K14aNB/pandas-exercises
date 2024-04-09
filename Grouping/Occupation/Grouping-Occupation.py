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
    setup(repo_path='pandas-exercises',nb_name='Grouping-Occupation')

# %% [markdown]
# **Read the data**

# %%
if 'google.colab' not in sys.modules:
    dir=os.path.join(os.getcwd(),'Data Science','Git Repos','pandas-exercises')
else:
    dir=os.getcwd()
users=pd.read_csv(os.path.join(dir,'data','u.user'),sep='|')

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
