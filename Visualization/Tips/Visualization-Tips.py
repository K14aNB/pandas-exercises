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
# # **Visualization - Tips**

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
result_path=env_setup.setup(repo_name='pandas-exercises',nb_name='Visualization-Tips')

# %% [markdown]
# **Read the data**

# %%
tips=pd.read_csv(os.path.join(result_path,'tips.csv'))

# %%
tips.head()

# %%
tips.info()

# %% [markdown]
# **Delete `Unnamed: 0` column**

# %%
tips=tips.drop(['Unnamed: 0'],axis=1)

# %% [markdown]
# **Plot the `total_bill` column histogram**

# %%
# Histogram of total_bill
fig=plt.figure(figsize=(10,5))
sns.histplot(x='total_bill',data=tips,kde=True)
plt.xlabel('Total Bill')
plt.ylabel('Count')
plt.title('Histogram of Total Bill')
plt.show()

# %% [markdown]
# **Create scatter plot presenting the relationship between `total_bill` and `tip`**

# %%
# Scatter plot of total_bill and tip
fig=plt.figure(figsize=(10,5))
sns.scatterplot(x='total_bill',y='tip',data=tips)
plt.xlabel('Total Bill')
plt.ylabel('Tips')
plt.title('Scatter plot between Total Bill and Tip')
plt.show()

# %% [markdown]
# **Create an image with relationship of `total_bill`, `tip` and `size`**

# %%
# Pair plot to describe the relationship of total_bill, tip, size
sns.pairplot(tips)
plt.show()

# %% [markdown]
# **Present the relationship between `days` and `total_bill`**

# %%
# Bar plot between days and total_bill
fig=plt.figure(figsize=(10,5))
sns.barplot(x='day',y='total_bill',data=tips)
plt.xlabel('Days of the Week')
plt.ylabel('Total Bill')
plt.title('Days of the Week vs Total Bill')
plt.show()

# %% [markdown]
# **Create a scatter plot with `day` as y-axis and `tip` as x-axis, differ the dots by sex**

# %%
# Scatter plot of tip and day
fig=plt.figure(figsize=(10,5))
sns.scatterplot(x='tip',y='day',hue='sex',data=tips)
plt.xlabel('Tips')
plt.ylabel('Day of the Week')
plt.title('Scatter plot of Tips vs Day of the Week')
plt.show()

# %% [markdown]
# **Create a box plot presenting the `total_bill` per `day` differentiating by the time (Dinner or Lunch)**

# %%
# Box plot of total_bill per day
fig=plt.figure(figsize=(10,5))
sns.boxplot(x='day',y='total_bill',hue='time',data=tips)
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.title('Total Bill per day')
plt.show()

# %% [markdown]
# **Create two Histograms of the `tip` value based on Dinner and Lunch. They must be side by side**

# %%
# Histograms for Dinner and Lunch presenting tip values
fig=plt.figure(figsize=(10,5))
grid=sns.FacetGrid(tips,col='time')
grid.map(plt.hist,'tip')
plt.show()

# %% [markdown]
# **Create two scatterplot graphs one for Male and other for Female presenting the `total_bill` value and `tip` relationship, differing by smoker or non-smoker.**

# %%
# Scatter plots for Male and Female presenting total_bill and tip based whether they are smoker or non-smoker
fig=plt.figure(figsize=(10,5))
grid=sns.FacetGrid(tips,col='sex',hue='smoker')
grid.map(plt.scatter,'total_bill','tip')
grid.add_legend()
plt.show()

# %%
