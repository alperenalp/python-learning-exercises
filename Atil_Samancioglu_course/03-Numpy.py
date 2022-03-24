#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ## numpy array

# In[2]:


benimListem = [20,30,40]


# In[3]:


type(benimListem)


# In[4]:


np.array(benimListem)


# In[5]:


matrixListesi=[[10,20,30],[20,30,40],[30,40,50]]


# In[6]:


matrixListesi[1]


# In[7]:


matrixListesi[1][0]


# In[8]:


np.array(matrixListesi)


# # Numpy Methodlar

# ## arange

# In[11]:


list(range(0,10))


# In[12]:


np.arange(0,10)


# In[13]:


np.arange(0,10,2)


# # zeros

# In[14]:


np.zeros(5)


# In[17]:


np.zeros((7,7))


# In[18]:


np.ones(5)


# In[20]:


np.ones((7,7))


# ## linspace

# In[22]:


np.linspace(0,20,6)


# In[23]:


np.linspace(0,10,20)


# ## eye

# In[24]:


np.eye(3)


# In[25]:


np.eye(10)


# ## random

# In[27]:


np.random.randn(5)


# In[28]:


np.random.randn(4,4)


# In[29]:


np.random.randint(1,10) ## 1 adet rastgele sayı üretme


# In[31]:


np.random.randint(1,300,5) ## 5 adet rastgele sayı üretme


# In[33]:


benimNumpyDizim = np.arange(30)


# In[34]:


benimNumpyDizim


# In[35]:


benimRandomDizim = np.random.randint(0,100,30)


# In[36]:


benimRandomDizim


#  ## numpy dizi methodları

# In[37]:


benimNumpyDizim.reshape(5,6)


# In[38]:


benimNumpyDizim.max()


# In[39]:


benimRandomDizim.max()


# In[40]:


benimRandomDizim.min()


# In[41]:


benimRandomDizim.argmax() ## maximum sayının kaçıncı indexte olduğunu bulur


# In[42]:


benimRandomDizim.argmin()


# In[44]:


benimNumpyDizim


# In[47]:


reshapeDizim=benimNumpyDizim.reshape(5,6)


# In[48]:


benimNumpyDizim.shape


# In[46]:


reshapeDizim


# In[49]:


reshapeDizim.shape


# # Numpy Indeksler

# In[50]:


benimDizim = np.arange(0,15)


# In[51]:


benimDizim


# In[52]:


benimDizim[5]


# In[54]:


benimDizim[3:7]


# In[55]:


benimDizim[3:8]=-5


# In[80]:


benimDizim


# In[81]:


baskaDizi = np.arange(0,24)


# In[82]:


baskaDizi


# In[83]:


slicingDizisi=baskaDizi[4:9]


# In[84]:


slicingDizisi


# In[85]:


slicingDizisi[:]=700


# In[86]:


slicingDizisi


# In[87]:


baskaDizi


# In[88]:


## numpy da kopya dizilerde yaptığımız değişikler orjinal diziyi de değiştirir


# In[89]:


ornekDizi = np.arange(0,24)


# In[99]:


ornekDiziKopyasi=ornekDizi.copy()  ## eğer orjinalde değişiklik olmasını
#istemiyorsak copy fonksiyonu ile kopyasını almamız gerekiyor.


# In[100]:


ornekDiziKopyasi


# In[101]:


ornekDizi


# In[102]:


ornekDiziKopyasiSlicing = ornekDiziKopyasi[3:6]


# In[103]:


ornekDiziKopyasiSlicing[:]=800


# In[104]:


ornekDiziKopyasiSlicing


# In[105]:


ornekDiziKopyasi


# In[106]:


ornekDizi


# # Matrix Indeksler

# In[118]:


benimListem = [[10,20,30],[20,30,40],[40,50,60]]


# In[119]:


benimMatrixDizim = np.array(benimListem)


# In[120]:


benimMatrixDizim


# In[121]:


benimMatrixDizim[0]


# In[122]:


benimMatrixDizim[1,2]


# In[123]:


benimMatrixDizim[1][2]


# In[124]:


benimMatrixDizim[1:,2]


# In[125]:


benimMatrixDizim[0:,2]


# In[126]:


benimMatrixDizim[2:,2]


# In[127]:


benimMatrixDizim[2:,0]


# In[130]:


benimMatrixDizim[2:,1:]


# In[133]:


benimMatrixDizim[2:,0:]


# In[134]:


yeniListe=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,17,19],[20,21,22,23,24]]


# In[135]:


yeniMatrix=np.array(yeniListe)


# In[136]:


yeniMatrix


# In[139]:


yeniMatrix[[0,2,4]]  ## istediğimiz yerleri liste olarak alabiliriz


# # Operasyonlar(Toplama,cikarma,kucuk,buyuk)

# In[151]:


yeniBirDizi=np.random.randint(1,100,20)


# In[152]:


yeniBirDizi


# In[153]:


yeniBirDizi>24


# In[158]:


sonucDizisi=yeniBirDizi>24


# In[159]:


sonucDizisi


# In[160]:


yeniBirDizi


# In[163]:


yeniBirDizi[sonucDizisi] ## dizinin içindeki true değerleri verir


# In[164]:


yeniBirDizi[yeniBirDizi>24]


# In[165]:


sonDizi=np.arange(0,24)


# In[166]:


sonDizi


# In[167]:


sonDizi+sonDizi


# In[168]:


sonDizi


# In[169]:


sonDizi*sonDizi


# In[170]:


sonDizi-sonDizi


# In[172]:


sonDizi/sonDizi


# In[173]:


np.sqrt(sonDizi)


# In[174]:


np.max(sonDizi)


# In[175]:


np.min(sonDizi)


# In[ ]:




