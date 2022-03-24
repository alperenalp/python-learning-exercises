#!/usr/bin/env python
# coding: utf-8

# ## Instance(nesne) & attribute(ozellik)

# In[ ]:


superKahramanAdi= "Superman"
superKahramanYasi=30
superKahramanMeslegi="Gazeteci"


# In[ ]:


class SuperKahraman():
    ozelGuc="Görünmezlik"
    def __init__(self,isim,yas,meslek):
        #nesne olusturdugumzda otomatik olarak çalışır
        print("init çağrıldı")
        self.isim=isim
        self.yas=yas
        self.meslek=meslek

    def ornekMetod(self):
        print(f"Ben süper kahramanım ve mesleğim: {self.meslek}")


# In[ ]:


superman= SuperKahraman("Superman",30,"Gazeteci")


# In[ ]:


superman.isim="Clark Kent"


# In[ ]:


superman.isim


# In[ ]:


superman.ozelGuc="Uçabilme"


# In[ ]:


superman.ozelGuc


# ## Methodlar

# In[ ]:


superman.ornekMetod()


# ## Default Değerler(self)

# In[ ]:


class Kopek():
    yilCarpani=7
    def __init__(self,yas=0):
        self.yas=yas
    
    def insanYasiHesapla(self):
        insanYasi=self.yas*self.yilCarpani
        print(f"Köpeğin insan yaşı: {insanYasi}")


# In[ ]:


benimKopek = Kopek()


# In[ ]:


benimKopek.yas


# In[ ]:


onunKopek=Kopek(5)


# In[ ]:


onunKopek.yas


# In[ ]:


onunKopek.insanYasiHesapla()


# # Inheritance(Kalıtım)

# In[ ]:


class Hayvan():
    def __init__(self):
        print("hayvan sınıfı init çağrıldı")
        
    def method1(self):
        print("hayvan sınıfı method1 çağrıldı")
        
    def method2(self):
        print("hayvan sınıfı method2 çağrıldı")


# In[ ]:


benimHayvan=Hayvan()


# In[ ]:


benimHayvan.method1()


# In[ ]:


benimHayvan.method2()


# In[ ]:


class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("kedi sınıfı init çağrıldı.")
        
    def miyavla(self):
        print("miyav")
        
    #override    
    def method1(self):
        print("kedi sınıfındaki method1 çağrıldı")


# In[ ]:


benimKedi=Kedi()


# In[ ]:


benimKedi.method1()


# In[ ]:


benimKedi.method2()


# In[ ]:


benimKedi.miyavla()


# ## Override(üzerinde yazma)

# In[ ]:


benimKedi.method1()


# # Polymorphism

# In[ ]:


#Aynı isimde methodların farklı amaca hizmet edebilmesidir.


# In[ ]:


class Elma():
    def __init__(self,isim):
        self.isim=isim
        
    def bilgiVer(self):
        return self.isim + " 100 kaloridir "
    


# In[ ]:


class Muz():
    def __init__(self,isim):
        self.isim=isim
        
    def bilgiVer(self):
        return self.isim + " 150 kaloridir "


# In[ ]:


elma = Elma("elma")


# In[ ]:


elma.bilgiVer()


# In[ ]:


muz = Muz("muz")


# In[ ]:


muz.bilgiVer()


# In[ ]:


meyveListesi=[elma,muz]


# In[ ]:


for meyve in meyveListesi:
    print(meyve.bilgiVer())


# In[ ]:


def bilgiAl(meyve):
    print(meyve.bilgiVer())
    


# In[ ]:


bilgiAl(muz)


# In[ ]:


bilgiAl(elma)


# ## Ozel Methodlar

# In[ ]:


class Meyve():
    def __init__(self,isim,kalori):
        self.isim=isim
        self.kalori = kalori
    
    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"
    
    def __len__(self):
        return self.kalori
    


# In[ ]:


muz = Meyve("Muz",150)


# In[ ]:


muz.kalori


# In[ ]:


print(muz)


# In[ ]:


benimListem = [1,2,3,"a",4.1]


# In[ ]:


print(benimListem)


# In[ ]:


len(benimListem)


# In[ ]:


len(muz)


# In[ ]:


elma = Meyve("Elma",200)


# In[ ]:


print(elma)


# In[ ]:


len(elma)


# # Hataları Ele Almak (try-except)

# In[ ]:


def toplama(numara1, numara2):
    return numara1+numara2


# In[ ]:


x=int(input("ilk numarayı giriniz: "))
y= int(input("ikinci numarayı giriniz: "))
toplama(x,y)


# ## try & except & else & finally

# In[1]:


while True:
    try:
        benimInt=int(input("Numaranızı giriniz: "))
    except:
        print("Lütfen yalnızca rakam giriniz!")
        continue
    else:
        print("Teşekkürler")
        break
    finally:
        print("finally çağrıldı.")
        


# # Libraries (Kutuphaneler)

# In[9]:


import numpy as np
import matplotlib.pyplot as matplot


# In[10]:


maasListesi = np.random.normal(4000,500,1000)
## Ortalama 4000 lira maaş çevresinde dolaşan ve 
## standart sapması 500 lira olan 1000 adet veri
numpy.mean(maasListesi)


# In[11]:


matplot.hist(maasListesi,50)
matplot.show()


# # Moduller ve Paketler

# In[ ]:




