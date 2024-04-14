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
# # **US - Baby Names**

# %% [markdown]
# **Check and install the dependencies**

# %%
# Check the current Runtime type
import os

try:
    if get_ipython().__class__.__module__=='google.colab._shell':
        runtime='colab'
        parent_path=os.path.join('/content','drive','MyDrive')
    elif get_ipython().__class__.__module__=='ipykernel.zmqshell':
        runtime='jupyter'
        parent_path=os.getcwd()
except NameError as ne:
    print('Running as .py Script and not as .ipynb Notebook')
    runtime='python-script'
    parent_path=os.path.join(os.path.expanduser('~'),'GDrive')

# %%
# !cat "$parent_path/Data Science/Git Repos/pandas-exercises/requirements.txt"

# %%
# If running as .py script, run this command in terminal first!
# !pip install -r "$parent_path/Data Science/Git Repos/pandas-exercises/requirements.txt"

# %% [markdown]
# **Import the libraries**

# %%
import pandas as pd
import env_setup

# %% [markdown]
# **Environment Setup**

# %%
# Setup environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_path='Data Science/Git Repos/pandas-exercises',nb_name='Stats-US-Baby-Names',runtime=runtime,parent_path=parent_path)

# %% [markdown]
# **Read the data**

# %%
baby_names=pd.read_csv(os.path.join(result_path,'US_Baby_Names_right.csv'))

# %%
baby_names.head()

# %%
baby_names.info()

# %% [markdown]
# **First 10 entries**

# %%
baby_names.head(10)

# %% [markdown]
# **Delete the column `Unamed: 0` and `Id`**

# %%
baby_names=baby_names.drop(columns=['Unnamed: 0','Id'])
baby_names

# %% [markdown]
# **Is there more male or female names in the dataset?**

# %%
baby_names.groupby('Gender')['Name'].agg('count')

# %% [markdown]
# **Group the dataset by `Name` and assign to `names`**

# %%
names=baby_names.groupby('Name')['Count'].sum()
names

# %% [markdown]
# **How many different names exist in the dataset?**

# %%
baby_names['Name'].nunique()

# %% [markdown]
# **What is the `Name` with most occurances?**

# %%
baby_names['Name'].value_counts().idxmax()

# %% [markdown]
# **How many different `Names` have the least occurrences?**

# %%
# TO DO

# %% [markdown]
# **What is the median of `Name` occurrence?**

# %%
baby_names['Count'].median()

# %%
baby_names.loc[baby_names['Count']==baby_names['Count'].median(),'Name']

# %% [markdown]
# **What is the standard deviation of names?**

# %%
baby_names['Count'].std()

# %% [markdown]
# **Summary**

# %%
baby_names['Count'].describe()

# %%
