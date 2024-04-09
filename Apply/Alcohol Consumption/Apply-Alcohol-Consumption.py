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
# # **Apply - Alcohol Consumption**

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
    setup(repo_path='pandas-exercises',nb_name='Apply-Alcohol-Consumption')

# %% [markdown]
# **Read the data**

# %%
if 'google.colab' not in sys.modules:
    dir=os.path.join(os.getcwd(),'Data Science','Git Repos','pandas-exercises')
else:
    dir=os.getcwd()
df=pd.read_csv(os.path.join(dir,'data','student-mat.csv'))

# %%
df.head()

# %%
df.info()

# %% [markdown]
# **Slice the dataframe from `school` till `guardian` column**

# %%
df=df.loc[:,'school':'guardian']
df

# %% [markdown]
# **Create a lambda function that will capitalize strings**

# %%
x = lambda string: string.capitalize()

# %% [markdown]
# **Capitalize both `Mjob` and `Fjob`**

# %%
df['Mjob']=df['Mjob'].apply(x)
df['Fjob']=df['Fjob'].apply(x)
df

# %% [markdown]
# **Print the last elements of the dataset**

# %%
df[-5:]


# %% [markdown]
# **Create a function called `majority` that returns a boolean value called `legal_drinker`   
# (Consider majority as older than 17 years)**

# %%
def majority(age:int):
    '''
    Checks age value and returns True if greater than 17 else returns False
    '''
    if age>17:
        return True
    else:
        return False


# %%
df['legal_drinker']=df['age'].apply(lambda x:majority(x))
df

# %% [markdown]
# **Multiply every numeric value in dataset by 10**

# %%
numeric=[col for col in df.columns if df[col].dtype in ['int32','int64','float32','float64']]
df[numeric]=df[numeric].apply(lambda x:x*10)
df

# %%
