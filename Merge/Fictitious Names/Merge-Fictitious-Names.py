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
import env_setup
import os

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and set output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Merge-Fictitious-Names')

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
merged_1=all_data.merge(data3,on='subject_id',how='inner')
merged_1

# %% [markdown]
# **Merge only the data that has same `subject_id` value on both `data1` and `data2`**

# %%
merged_2=data1.merge(data2,on='subject_id',how='inner')
merged_2

# %% [markdown]
# **Merge all values in `data1` and `data2`, with matching records from both sides where available**

# %%
merged_3=data1.merge(data2,on='subject_id',how='outer')
merged_3

# %%
