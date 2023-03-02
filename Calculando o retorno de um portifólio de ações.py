#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[4]:


tickers = ['PG','MSFT','F','GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source= 'iex', start= '2010-1-1',api_key = 'pk_a3d7d3d2cf6348fdb21fc1361e97e107')['close']


# In[13]:


mydata.info()


# In[6]:


mydata.head()


# In[7]:


mydata.tail()


# Normalizar dados para base 100

# In[17]:


mydata.iloc[0]
#este comando nos fornece os dados da primeira linha


# In[23]:


((mydata/ mydata.iloc[0])*100).plot(figsize = (15,6));
plt.show()
#plotamos no quesito porcentagem de aumento e não no quesito valor do ativo somente


# # Calculando retornos simples destas ações

# In[33]:


returns = (mydata/mydata.shift(1))-1
returns.head()


# In[34]:


weights = np.array([0.25, 0.25, 0.25, 0.25])


# In[37]:


annual_returns = returns.mean() * 250
annual_returns


# In[38]:


np.dot(annual_returns, weights)
#o dot faz o calculo do produto vetorial ou de matriz


# In[44]:


pfolio_1 = str(round(np.dot(annual_returns, weights),5)*100) + ' %'
print(pfolio_1)


# Comparando outros pesos nas ações da carteira

# In[45]:


weights_2 = np.array([0.4, 0.4, 0.15, 0.05])


# In[46]:


pfolio_2 = str(round(np.dot(annual_returns, weights_2),5)*100) + ' %'
print(pfolio_2)

