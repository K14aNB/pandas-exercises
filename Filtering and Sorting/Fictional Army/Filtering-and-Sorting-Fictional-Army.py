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
# # **Filtering and Sorting - Fictional Army**

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
    setup(repo_path='pandas-exercises',nb_name='Filtering-and-Sorting-Fictional-Army')

# %% [markdown]
# **Read the data**

# %%
# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

# %%
# Create a dataframe army from raw_data
army=pd.DataFrame(raw_data,columns=['regiment','company','deaths','battles','size','veterans','readiness','armored','deserters','origin'])

# %%
army.head()

# %%
army.info()

# %% [markdown]
# **Set `origin` column as index**

# %%
army=army.set_index('origin')
army

# %% [markdown]
# **Print only the `veterans` columns**

# %%
army.loc[:,['veterans']]

# %% [markdown]
# **Print `veterans` and `deaths` columns**

# %%
army.loc[:,['veterans','deaths']]

# %% [markdown]
# **Print the name of all columns**

# %%
army.columns.to_list()

# %% [markdown]
# **Select `deaths`, `size` and `deserters` columns from Maine and Alaska**

# %%
army.loc[['Maine','Alaska'],['deaths','size','deserters']]

# %% [markdown]
# **Select rows 3 to 7 and columns 3 to 6**

# %%
army.iloc[2:7,2:6]

# %% [markdown]
# **Select every row after the 4th row and all columns**

# %%
army.iloc[4:,:]

# %% [markdown]
# **Select every row upto 4th row and all columns**

# %%
army.iloc[:4,:]

# %% [markdown]
# **Select 3rd column upto 7th column**

# %%
army.iloc[:,2:7]

# %% [markdown]
# **Select rows where `deaths` are greater than 50**

# %%
army.loc[army['deaths']>50]

# %% [markdown]
# **Select rows where `deaths` are greater than 500 or less than 50**

# %%
army.loc[(army['deaths']>500) | (army['deaths']<50)]

# %% [markdown]
# **Select all regiments not named 'Dragoons'**

# %%
army.loc[army['regiment']!='Dragoons']

# %% [markdown]
# **Select rows Texas and Arizona**

# %%
army.loc[['Arizona','Texas']]

# %% [markdown]
# **Select 3rd cell in the row named 'Arizona'**

# %%
army.loc['Arizona',army.columns[2]]

# %% [markdown]
# **Select 3rd cell down in the column named `deaths`**

# %%
army.loc[army.index[2],'deaths']

# %%
