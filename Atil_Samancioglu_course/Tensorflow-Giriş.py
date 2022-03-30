#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_excel("bisiklet_fiyatlari.xlsx")


# In[3]:


df.head()


# In[4]:


import seaborn as sbn
import matplotlib.pyplot as plt


# In[5]:


sbn.pairplot(df)


# # Veriyi eğitim ve test olarak ikiye ayırma

# In[6]:


from sklearn.model_selection import train_test_split


# In[7]:


# y = wx + b
# y -> label
y = df["Fiyat"].values

# x -> feature (özellik)
x = df[["BisikletOzellik1", "BisikletOzellik2"]].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=15)


# In[8]:


x_train.shape


# In[9]:


x_test.shape


# In[10]:


y_train.shape


# In[11]:


y_test.shape


# In[12]:


#scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


# In[13]:


scaler.fit(x_train)


# In[14]:


x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)


# In[15]:


x_train


# In[16]:


import tensorflow as tf


# In[17]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[18]:


model = Sequential()

model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))

model.add(Dense(1))

model.compile(optimizer="rmsprop", loss="mse")


# In[19]:


#Epocs dengeli olmalı çok fazla geçilirse overfit olabilir ezber olabilir
#batch eğitim için çalışılacak grup miktarı veri seti arttıkça arttırılabilir
model.fit(x_train, y_train, epochs=250)


# In[24]:


#alt satırdaki kod loss oranlarını sözlük içersinde verir diziye çevirdik
loss= model.history.history["loss"]


# In[25]:


sbn.lineplot(x=range(len(loss)), y=loss)


# In[29]:


trainLoss= model.evaluate(x_train, y_train, verbose=0)
trainLoss


# In[30]:


testLoss = model.evaluate(x_test, y_test, verbose=0)
testLoss


# In[31]:


testTahminleri = model.predict(x_test)


# In[32]:


testTahminleri


# In[34]:


tahminDF = pd.DataFrame(y_test, columns=["Gerçek Y"])


# In[35]:


tahminDF


# In[37]:


testTahminleri = pd.Series(testTahminleri.reshape(330,))


# In[38]:


testTahminleri


# In[39]:


tahminDF = pd.concat([tahminDF, testTahminleri], axis=1)


# In[41]:


tahminDF.columns = ["Gerçek Y", "Tahmin Y"]


# In[42]:


tahminDF


# In[43]:


sbn.scatterplot(x="Gerçek Y", y="Tahmin Y", data=tahminDF)


# In[44]:


from sklearn.metrics import mean_absolute_error, mean_squared_error


# In[45]:


mean_absolute_error(tahminDF["Gerçek Y"], tahminDF["Tahmin Y"])


# In[46]:


mean_squared_error(tahminDF["Gerçek Y"], tahminDF["Tahmin Y"])


# In[47]:


df.describe()


# In[48]:


yeniBisiklet = [[1751, 1750]]


# In[49]:


yeniBisiklet = scaler.transform(yeniBisiklet)


# In[50]:


model.predict(yeniBisiklet)


# In[51]:


from tensorflow.keras.models import load_model


# In[52]:


model.save("bisiklet_modeli.h5")


# In[53]:


CagrilanModel = load_model("bisiklet_modeli.h5")


# In[54]:


CagrilanModel.predict(yeniBisiklet)


# In[ ]:




