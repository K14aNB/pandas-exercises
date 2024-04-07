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
# **Import the libraries**

# %%
import pandas as pd
import os
import sys
from urllib3 import PoolManager,request

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment
# Github gist url for Python Script which will perform environment setup
env_url='https://gist.githubusercontent.com/K14aNB/46becb626d36ad8fa8d445616241dfef/raw/'
http=PoolManager()
env_setup_response=http.request('GET',env_url)
if env_setup_response.status==200:
    exec(env_setup_response.data.decode('utf-8'))
    setup(repo_path='pandas-exercises',nb_name='World-Food-Facts')

# %% [markdown]
# **Read the data**

# %%
if 'google.colab' not in sys.modules:
    dir=os.path.join(os.getcwd(),'Data Science','Git Repos','pandas-exercises')
else:
    dir=os.getcwd()
food = pd.read_csv(os.path.join(dir,'data','en.openfoodfacts.org.products.tsv'),sep='\t',low_memory=False)

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
