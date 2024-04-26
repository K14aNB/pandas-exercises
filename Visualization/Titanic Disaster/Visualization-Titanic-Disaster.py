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
# # **Visualization - Titanic Disaster**

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
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Visualization-Titanic-Disaster')

# %% [markdown]
# **Read the data**

# %%
titanic=pd.read_csv(os.path.join(result_path,'train.csv')).set_index('PassengerId',drop=True)

# %%
titanic.head()

# %%
titanic.info()

# %% [markdown]
# **Create a Pie Chart presenting the Male/Female proportion**

# %%
# Finding the proportion of Male and Female
sex_ratio=titanic['Sex'].value_counts(normalize=True)

# %%
# Pie plot of Male/Female Proportion
fig=plt.figure(figsize=(10,5))
plt.pie(sex_ratio,labels=sex_ratio.index,autopct='%.2f%%')
plt.title('Pie Chart of Male/Female proportion')
plt.show()

# %% [markdown]
# **Create a scatter plot of `Fare` and `Age`, differ the color by `Sex`**

# %%
# Scatter plot of Fare and Age
fig=plt.figure(figsize=(10,5))
sns.scatterplot(x='Age',y='Fare',hue='Sex',data=titanic)
plt.title('Scatter plot of Age vs Fare')
plt.show()

# %% [markdown]
# **How many people `Survived`?**

# %%
titanic['Survived'].sum()

# %% [markdown]
# **Create a Histogram with `Fare`**

# %%
# Histogram with Fare
fig=plt.figure(figsize=(10,5))
sns.histplot(x='Fare',data=titanic,bins=40,kde=True)
plt.xlabel('Fare paid')
plt.title('Histogram of Fare paid')
plt.show()

# %%
