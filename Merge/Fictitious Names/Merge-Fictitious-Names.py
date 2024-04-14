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
# # **Merge - Fictitious Names**

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
# Github gist for Python Script which will perform environment setup
env_url='https://gist.githubusercontent.com/K14aNB/46becb626d36ad8fa8d445616241dfef/raw/'
http=PoolManager()
response=http.request('GET',env_url)
if response.status==200:
    exec(response.data.decode('utf-8'))
    setup(repo_path='pandas-exercises',nb_name='Merge-Fictitious-Names')

# %% [markdown]
# **Read the data**

# %%
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

# %%
data1=pd.DataFrame(raw_data_1,columns=['subject_id','first_name','last_name'])
data2=pd.DataFrame(raw_data_2,columns=['subject_id','first_name','last_name'])
data3=pd.DataFrame(raw_data_3,columns=['subject_id','first_name','last_name'])

# %%
data1.head()

# %%
data1.info()

# %%
data2.head()

# %%
data2.info()

# %%
data3.head()

# %%
data3.info()

# %% [markdown]
# **Join two dataframes `data1` and `data2` along rows and assign to `all_data`**

# %%
all_data=pd.concat([data1,data2]).reset_index(drop=True)
all_data

# %% [markdown]
# **Join two dataframes `data1` and `data2` along columns and assign to `all_data_cols`**

# %%
all_data_cols=pd.concat([data1,data2],axis=1)
all_data_cols

# %% [markdown]
# **Print data3**

# %%
data3

# %% [markdown]
# **Merge `all_data` and `data3` along the `subject_id` value**

# %%
merged=all_data.merge(data3,on='subject_id',how='inner')
merged

# %%
