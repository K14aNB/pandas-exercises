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
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Apply-Alcohol-Consumption')

# %% [markdown]
# **Read the data**

# %%
df=pd.read_csv(os.path.join(result_path,'student-mat.csv'))

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
