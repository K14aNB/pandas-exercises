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
# # **Apply - US Crime Rates**

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
    setup(repo_path='pandas-exercises',nb_name='Apply-US-Crime-Rates')

# %% [markdown]
# **Read the data**

# %%
if 'google.colab' not in sys.modules:
    dir=os.path.join(os.getcwd(),'Data Science','Git Repos','pandas-exercises')
else:
    dir=os.getcwd()
crime=pd.read_csv(os.path.join(dir,'data','US_Crime_Rates_1960_2014.csv'))

# %%
crime.head()

# %%
crime.info()

# %% [markdown]
# **What is the datatypes of columns**

# %%
crime.dtypes

# %% [markdown]
# **Convert the type of the column `Year` to datetime64**

# %%
crime['Year'] = pd.to_datetime(crime['Year'],format='%Y')

# %%
crime['Year'].dtype

# %%
crime['Year'].head()

# %% [markdown]
# **Set the `Year` column as index of the dataframe**

# %%
crime=crime.set_index('Year')
crime.head()

# %% [markdown]
# **Delete the `Total` column**

# %%
crime=crime.drop(['Total'],axis=1)
crime.head()

# %% [markdown]
# **Group the `Year` by decades and sum the values**

# %%
# Convert %Y-%m-%d into %Y
list_of_yrs=crime.index.to_list()
list_of_yrs=list(map(lambda x:str(x).split('-')[0],list_of_yrs))

# %%
# Turn Years into Decades
list_of_decades=list(map(lambda x:round(int(x),-1),list_of_yrs))

# %%
# Make a copy of dataframe before changing index from years to decades
crime_dec=crime.copy()

# %%
# Set list of decades as index of crime_dec
crime_dec=crime_dec.set_index([list_of_decades])

# %%
# Group by decades
groupby_dec=crime_dec.groupby(crime_dec.index).sum()

# %%
# Replace Population value by max value in the column
groupby_pop=crime_dec.groupby(crime_dec.index)['Population'].max()
groupby_dec['Population']=groupby_pop

# %%
groupby_dec

# %%
