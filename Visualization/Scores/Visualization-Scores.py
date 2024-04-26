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
# # **Visualization - Scores**

# %% [markdown]
# **Check and install the dependencies**

# %%
# !curl -sSL https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt

# %%
# Run this command in terminal before running this notebook as .py script
# Installs dependencies from requirements.txt present in the repo
# %%capture
# !pip install -r https://raw.githubusercontent.com/K14aNB/pandas-exercises/main/requirements.txt

# %% [markdown]
# **Import the libraries**

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import env_setup

# %% [markdown]
# **Environment Setup**

# %%
# Setup Environment(Downloading data and setting output formats specified in config.yaml)
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Visualization-Scores')

# %% [markdown]
# **Read the data**

# %%
score_data={
    'first_name':['Jason','Molly','Tina','Jake','Amy'],
    'last_name':['Miller','Jacobson','Ali','Milner','Cooze'],
    'age': [42,52,36,24,73],
    'female':[0,1,1,0,1],
    'preTestScore':[4,24,31,2,3],
    'postTestScore':[25,94,57,62,70]
}

# %%
scores=pd.DataFrame(score_data,columns=['first_name','last_name','age','female','preTestScore','postTestScore'])

# %%
scores.head()

# %%
scores.info()

# %% [markdown]
# **Create a scatter plot of `preTestScore` and `postTestScore`, with size of each point determined by `age`**

# %%
# Scatter plot of preTestScore and postTestScore
fig=plt.figure(figsize=(10,5))
sns.scatterplot(x='preTestScore',y='postTestScore',data=scores,size='age')
plt.xlabel('Pre Test Scores')
plt.ylabel('Post Test Scores')
plt.title('Pre Test Scores vs Post Test Scores')
plt.show()

# %% [markdown]
# **Create a scatter plot of `preTestScore` and `postTestScore` with size of each point determined by 4.5 times `postTestScore` and color by sex**

# %%
# Scatter plot of preTestScore and postTestScore
fig=plt.figure(figsize=(10,5))
sns.scatterplot(x='preTestScore',y='postTestScore',data=scores,size=scores['postTestScore']*4.5,hue='female')
plt.xlabel('Pre Test Scores')
plt.ylabel('Post Test Scores')
plt.title('Pre Test Scores vs Post Test Scores')
plt.show()

# %%
