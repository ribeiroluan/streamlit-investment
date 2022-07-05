#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import plotly.express as px


# ## Parameters

# In[371]:


#Creating variables to store start and end date of analysis
start_date = '2022-01-01'
end_date = date.today()


# In[369]:


#We are going to store all the tickers for the companies in our investment portfolio in a variable named wallet. Later, we will iterate over this variable in order to pull our data
wallet = ['CIEL3', 'BRFS3', 'BBDC4', 'ENEV3']


# ## First, let's pull data for our reference index (IBOVESPA)

# In[372]:


#Reading data using pandas datareader and cleaning column names
ibov = pdr.DataReader(f'^BVSP', data_source='yahoo', start=start_date, end=end_date)
ibov.reset_index(drop=False, inplace=True)
ibov = ibov[['Date', 'Close']] #we are only interested in the closing prices
ibov.rename(columns={'Date':'date', 'Close':'ibov_close'}, inplace=True)


# In[373]:


#Creating the cumulative change column. This way, we can easily compare performance across multiple companies
reference = ibov.at[0,"ibov_close"]
ibov['ibov_cum_change'] = ibov['ibov_close'].apply(lambda x: (x-reference)*100/reference)
ibov


# ## Now, let's pull data for our investment portfolio

# In[374]:


df_holder = []

for stock in wallet:
    #Reading data and cleaning column names
    temp_df = pdr.DataReader(f'{stock}.SA', data_source='yahoo', start=start_date, end=end_date)
    temp_df.reset_index(drop=False, inplace=True)
    temp_df = temp_df[['Date', 'Close']]
    temp_df.rename(columns={'Date':'date', 'Close':f'{stock}_close'}, inplace=True)
    
    #Creating the cumulative change column
    reference = temp_df.at[0,f'{stock}_close']
    temp_df[f'{stock}_cum_change'] = temp_df[f'{stock}_close'].apply(lambda x: (x-reference)*100/reference)
    
    #Appending our temporary dataframe to our empty list, which will be later concatenated
    df_holder.append(temp_df)
    
#Lastly, lets concat our temp dataframes dropping duplicates - date column
wallet_df = pd.concat(df_holder, axis=1).T.drop_duplicates().T
wallet_df


# In[375]:


#Finally, let's merge the index dataframe with our wallet dataframe
final_df = pd.merge(ibov, wallet_df, on='date')
final_df.iloc[:,1:].apply(pd.to_numeric)
for column in final_df.columns:
    if column not in ['date']:
        final_df[column] = final_df[column].astype(float)
final_df


# In[376]:


#Computing total change
total_change_columns = [column for column in final_df.columns if "change" in column and column not in ['ibov_cum_change', 'total_cum_change']]
final_df['total_cum_change'] = final_df[total_change_columns].mean(axis=1)
final_df


# ## Investment results

# In[378]:


changes = [final_df[column] for column in final_df.columns if "change" in column and column not in ['ibov_cum_change','total_cum_change']]
changes = pd.concat(changes, axis=1)
changes_results = changes.iloc[-1].sort_values(ascending=False)


# In[379]:


print(f'A ação do seu portfólio que teve melhor desempenho no período foi a {changes_results.index[0].split("_")[0]}, com um rendimento de {round(changes_results[0],2)}%.')


# In[380]:


print(f'A ação do seu portfólio que teve pior desempenho no período foi a {changes_results.index[-1].split("_")[0]}, com um rendimento de {round(changes_results[-1],2)}%.')


# In[381]:


print(f'O seu portfólio teve um desempenho médio de {round(final_df["total_cum_change"].iloc[-1],2)}% no período, {round(final_df["total_cum_change"].iloc[-1]-final_df["ibov_cum_change"].iloc[-1],2)}% comparado ao Ibovespa.')


# ## Visualizing data

# In[382]:


fig = px.line(final_df, x='date', y=[column for column in final_df.columns if "close" in column and "ibov" not in column])
fig.show()


# In[383]:


fig = px.line(final_df, x='date', y=[column for column in final_df.columns if "change" in column])
fig.show()

