#!/usr/bin/env python
# coding: utf-8

# ## Veriables(Değişkenler)

# ## Integer ve float

# In[ ]:


degisken=10


# In[3]:


digerdegisken=20


# In[4]:


degisken + digerdegisken


# In[5]:


type(degisken)


# In[9]:


sonuc=digerdegisken/degisken


# In[10]:


sonuc


# In[11]:


type(sonuc)


# In[12]:


a=5
pi=3.14


# In[13]:


a/pi


# python farklı veri tiplerini de bölebilir

# ## Matematiksel İşlemler

# In[15]:


x=5
y=3


# In[16]:


x*x*x*x


# In[17]:


x ** 4


# In[18]:


## x üzeri 4 ü hesapladık


# In[30]:


## Remainder(Kalanını Bulmak)


# In[19]:


10%2


# In[20]:


11%2


# In[21]:


11%3


# In[22]:


kullanicinin_yasi=10


# In[24]:


## camelCase ve snake_case yazim raconları vardır 
## pythoncular genellikle camelCase kullanır


# In[28]:


kullaniciYasi = input("Yaşınızı Giriniz: ")


# In[29]:


type(kullaniciYasi)


# ## String

# In[31]:


"Merhaba Dünya"


# In[32]:


x= "Merhaba Dünya"


# In[33]:


## daha önce x'i int veri tipinde kullanmıştık 
## ama python'ın kolaylığı sayayesinde string atayabildik 


# In[34]:


x=10


# In[35]:


x="hello"


# In[36]:


type(x)


# In[37]:


y='yeni string'


# In[38]:


type(y)


# In[39]:


"Atıl'ın Yeri"


# In[40]:


## Tek tırnak çift tırnak açmadan önce string ifade yazarken kullanacağın
## cümleye göre tırnak açılmalı


# In[41]:


a=5


# In[42]:


y.capitalize


# In[43]:


y.capitalize()


# In[44]:


## capitalize fonksiyonu ilk harfi büyük yapar


# In[45]:


myString="Alperen ALP"


# In[46]:


myString+y


# ## Veri tiplerini birbirine dönüştürme işlemi

# In[47]:


myInput=input("Yaşınızı Giriniz: ")


# In[48]:


type(myInput)


# In[49]:


myIntInput= int(myInput)


# In[50]:


type(myIntInput)


# In[51]:


myIntInput


# In[ ]:


## string uzunluk bulma


# In[53]:


k = "Samancıoğlu"


# In[54]:


len(k)


# In[55]:


print("Merhaba \nPython")


# ## Slicing Videosu 

# ## Indexleme

# In[57]:


isim= "Atıl Samancıoğlu"


# In[58]:


isim


# In[59]:


isim[0]


# In[60]:


isim[7]


# In[61]:


isim[-1]


# In[62]:


## pythona özel -1 yazarsak string ifadenin son karakterini getirir


# ## Slicing Kesme

# In[63]:


yeniString="0123456789"


# In[64]:


yeniString[2:]


# In[65]:


harfString="abcdefgh"


# In[66]:


harfString[3:]


# In[67]:


harfString[:3]


# In[69]:


gelenVeri= "AhmetinYasi45"


# In[70]:


gelenVeri[-2:]


# In[71]:


gelenVeri[2:5]


# In[72]:


## gelenVeri[2:5] deki 2 başlangıç indexi 5 bitiş indexi


# In[74]:


gelenVeri[::3]


# In[76]:


## Step Size 3 er 3 er atlayarak yazdırma


# In[77]:


gelenVeri[::-1]


# In[78]:


## step size ile tersten yazma


# In[1]:


benimIsmim = "alperen"


# In[2]:


benimIsmim


# In[3]:


benimIsmim.capitalize()


# In[4]:


benimIsmim=benimIsmim.capitalize()


# In[5]:


benimIsmim


# In[6]:


benimTamIsmim="Alperen Alp"


# In[7]:


benimTamIsmim.split()


# In[8]:


benimTamIsmim.upper()


# ## Listeler

# In[11]:


nestedList=[1,5,"atıl",4,[6,"z"]]


# In[12]:


listedenAl=nestedList[4][1];


# In[13]:


listedenAl


# ## Sözlükler

# In[14]:


Yemeklerim = ["Elma", "Karpuz", "Muz"]


# In[15]:


Kalorilerim = [100,200,300]


# In[16]:


Yemeklerim[1
        ]


# In[17]:


Kalorilerim[1]


# In[18]:


## bu şekilde bir uygulamamız olsun çok büyük veri setlerinde 
## ya kalori indeksi kaysaydı sıkıntı yaşardık


# In[19]:


##dictionary(sözlük) burda devreye girer


# In[20]:


sozluk = {"anahtarKelime":"deger"}


# In[21]:


type(sozluk)


# In[24]:


sozluk["anahtarKelime"]


# In[25]:


YemekKaloriSozlugum={"elma":100, "karpuz":200, "muz":300}


# In[26]:


YemekKaloriSozlugum["muz"]


# In[27]:


YemekKaloriSozlugum["elma"]=500


# In[28]:


YemekKaloriSozlugum


# In[29]:


yeniDictionary = {"anahtar1":100, "anahtar2": [10,20,30,40,4.5,"atıl"],"anahtar3":{"anahtar9":4}}


# In[30]:


yeniDictionary.keys()


# In[31]:


yeniDictionary.values()


# In[32]:


yeniDictionary["anahtar2"][5]


# In[33]:


yeniDictionary["anahtar3"]["anahtar9"]


# ## Set Koleksiyonu

# In[34]:


benimListem= [1,2,3,1,2,3]


# In[35]:


benimListem


# In[36]:


setListem=set(benimListem)


# In[37]:


setListem


# In[38]:


type(benimListem)


# In[39]:


type(setListem)


# In[40]:


benimSet={"a","b","c"}


# In[41]:


type(benimSet)


# ## Tuple Koleksiyonu

# In[42]:


## Listeye çok benzer tek farkı Liste içindeki değerler değiştirilemez.


# In[1]:


benimTuple = (1,2,"a",4.5)


# In[2]:


benimTuple


# In[3]:


benimTuple[0]=100


# ## Boolean

# In[4]:


benimBoolean = True


# In[5]:


type(benimBoolean)


# ## Eğer Kontrolleri

# In[6]:


karakterCanli=True


# In[10]:


if karakterCanli:
    print("Karakter Yaşıyor")
else:
    print("Karakter Yaşamıyor")


# In[14]:


benimString = "Atıl Samancıoğlu"


# In[15]:


if benimString == "atıl samancıoğlu":
    print("eşitmiş")
else:
    print("eşit değilmiş")


# In[16]:


if "cıoğlu" in benimString:
    print("varmış")
else:
    print("yokmuş")


# In[17]:


benimListem = [10,20,30,40,50]


# In[18]:


if 10 in benimListem:
    print("evet var")


# In[19]:


benimSozluk = {"muz":100,"elma":150,"karpuz":500}


# In[20]:


if "muz" in benimSozluk.keys():
    print("varmış")


# In[21]:


if 500 in benimSozluk.values():
    print("var kardeş")


# # For Döngüsü 

# In[3]:


yeniListe=[1,2,3,4,5,6]


# In[4]:


for num in yeniListe:
    if num%2==0:
        print(num)
    


# In[5]:


yeniString = "Alperen"


# In[6]:


for harf in yeniString:
    print(harf)


# In[7]:


koordinatListesi=[(10.2,15.2),(32.4,16.2),(40.2,20.2)]


# In[9]:


type(koordinatListesi[0])


# In[10]:


for eleman in koordinatListesi:
    print(eleman)


# In[11]:


for (x,y) in koordinatListesi:
    print(x)


# In[12]:


benimSozluk={"muz":150, "portakal":250, "elma":400}


# In[13]:


benimSozluk.items()


# In[14]:


## Tuple olarak verdi


# In[15]:


for(anahtar, deger) in benimSozluk.items():
    print(deger)


# In[20]:


benimListem=[5,10,15,20,25,30]


# In[21]:


for numara in benimListem:
    if numara==15:
        continue
    print(numara)


# ## While Dongusu

# In[22]:


x=0
while x<10:
    print(x)
    x=x+1


# In[23]:


benimListem=[1,2,3,4,5]


# In[24]:


benimListem.pop()


# In[ ]:





# In[25]:


benimListem


# In[26]:


benimListem.append(99)


# In[27]:


benimListem


# In[28]:


while 3 in benimListem:
    print("3 hala listenin içerisinde")
    benimListem.pop()


# In[29]:


numara=0
while numara < 5:
    if numara ==4:
        break
    print(numara)
    numara+=1


# In[35]:


yeniDegisken=0
while yeniDegisken<15:
    #print("yeniDegiskenin'in güncel değeri: " + str(yeniDegisken)) 
    #Ustteki sekilde de yapılabilir
    print(f"yeniDegiskenin'in güncel değeri: {yeniDegisken}")
    yeniDegisken+=1


# ## Veri Bilimi Onemli Metodlar

# In[ ]:


# Range metodu


# In[40]:


range(15)


# In[41]:


list(range(15))


# In[42]:


list(range(5,22,2))


# In[43]:


## enumerate


# In[44]:


index=0
for numara in list(range(5,15)):
    print(f"güncel numara: {numara} güncel index: {index}")
    index+=1


# In[47]:


for eleman in enumerate(list(range(5,15))):
    print(eleman)


# In[48]:


for (index,numara) in enumerate(list(range(5,15))):
    print(index)


# # Random

# In[49]:


from random import randint


# In[50]:


randint(0,100)


# In[51]:


from random import shuffle


# In[52]:


yeniListe= list(range(0,10))


# In[53]:


yeniListe


# In[56]:


shuffle(yeniListe)


# In[57]:


yeniListe


# # İleri seviye işlemler

# In[58]:


# Zip


# In[60]:


yemekListesi=["muz", "ananas", "elma"]
kaloriListesi=[100,200,300]
gunListesi=["pazartesi","salı","çarşamba"]


# In[64]:


ziplenmisListe=list(zip(yemekListesi,kaloriListesi,gunListesi))


# In[65]:


ziplenmisListe


# In[66]:


# Listeler


# In[70]:


listeOrnegi=[]
benimString="atıl samacıoğlu"

for harf in benimString:
    listeOrnegi.append(harf)


# In[71]:


listeOrnegi


# In[72]:


yeniString = "atıl samancıoğlu"


# In[73]:


yeniListeOrnegi = [eleman for eleman in yeniString]


# In[74]:


yeniListeOrnegi


# In[75]:


ikinciListeOrnegi=[numara*5 for numara in list(range(0,10))]


# In[76]:


ikinciListeOrnegi


# # Fonksiyonlar

# In[77]:


benimAdim="Alperen Alp"


# In[79]:


benimAdim.upper()


# In[80]:


def ilkFonksiyon():
    print("ilk fonksiyonum")


# In[81]:


ilkFonksiyon()


# ## input & return

# In[82]:


def merhabaDunya(yazdirilacakIsim):
    print("merhaba")
    print(yazdirilacakIsim)


# In[83]:


merhabaDunya("Atıl")


# In[84]:


def merhaba(isim="atıl"):
    print("merhaba")
    print(isim)


# In[85]:


merhaba()


# In[86]:


merhaba("python")


# In[88]:


def toplama(num1,num2):
    sonuc = num1+num2
    print(sonuc)


# In[90]:


toplama(10,20)


# In[91]:


def dondurmeliToplama(num1,num2):
    return num1+num2


# In[92]:


yeniSonuc=dondurmeliToplama(10,20)


# In[93]:


print(yeniSonuc)


# # args & kwargs

# In[94]:


def yeniToplama(*args):
    return sum(args)


# In[95]:


yeniToplama(10,20,30,40,50,60)


# In[96]:


yeniToplama(10,20)


# In[99]:


def benimFonksiyonum(*args):
    return args


# In[100]:


type(benimFonksiyonum(20,30,40))


# In[101]:


def ornekFonksiyon(**kwargs):
    return kwargs


# In[102]:


type(ornekFonksiyon(muz=100, elma=200, ananas=300))


# In[105]:


def keyWordKontrolu(**kwargs):
    if "atıl" in kwargs:
        print("atıl var")
    else:
        print("atıl yok")


# In[106]:


keyWordKontrolu(atıl=70,zeynep=50,mehmet=40)


# # Önemli Fonksiyonlar

# In[107]:


def bolmeIslemi(numara):
    return numara/2


# In[108]:


bolmeIslemi(20)


# In[109]:


benimListem=[1,2,3,4,5,6,7,8,9,10]


# In[110]:


yeniListe=[]
for eleman in benimListem:
    yeniListe.append(bolmeIslemi(eleman))


# In[111]:


yeniListe


# map Fonksiyonu

# In[123]:


#listedeki elemanları hızlıca fonksiyona sokup sonucları tekrar liseye atar


# In[122]:


list(map(bolmeIslemi, benimListem))


# In[115]:


def kontrolFonksiyonu(string):
    return "a" in string


# In[116]:


kontrolFonksiyonu("atıl")


# In[117]:


stringListesi=["atıl","samancıoğlu","atlass","zeynep","mehmet","ahmet","levent"]


# In[119]:


sonucListesi=list(map(kontrolFonksiyonu,stringListesi))


# In[120]:


sonucListesi


# In[121]:


sonucListesi.count(True)


# Filter fonksiyonu

# In[124]:


list(filter(kontrolFonksiyonu,stringListesi))


# In[125]:


#true olan sonucları filtreler


# lambda Fonksiyonu

# In[126]:


carpma=lambda numara:numara*3


# In[127]:


carpma(10)


# In[128]:


ornekListesi=[10,20,30]


# In[129]:


list(map(lambda numara:numara*4, ornekListesi))


# # Kapsam (Scope)

# In[131]:


numara=20
def carpma(rakam):
    numara=10
    return numara*rakam


# In[132]:


carpma(5)


# In[133]:


print(numara)


# In[134]:


x=20
x=10


# In[135]:


x


# Local, Enclosing, Global, Built-In Modeli

# In[140]:


benimAdim = "Atıl"
#Global değişken

def benimFonksiyonum():
    benimAdim = "Alperen"
    #Enclosing
    def icFonksiyon():
        benimAdim="Ayşe"
        #Local
        print(benimAdim)
    icFonksiyon()


# In[141]:


benimFonksiyonum()


# In[142]:


print(benimAdim)


# In[151]:


y=10
def yeniFonksiyon(y):
    print(y)
    y=5
    print(y)
    return y


# In[152]:


yeniFonksiyon(3)


# In[153]:


#Globaldeki değişkeni değiştirme


# In[154]:


y


# In[155]:


y=yeniFonksiyon(3)


# In[156]:


y


# In[157]:


y=10
def ornekFonksiyon():
    global y
    y=5
    print(y)


# In[158]:


ornekFonksiyon()


# In[159]:


y


# # Hesap Makinesi

# In[191]:


def hesapla(a,b,islem):
    if islem=="+":
        return(f"{a} + {b} = {a+b}")
    if islem =="-":
        return(f"{a} - {b} = {a-b}")
    if islem=="*":
        return(f"{a} * {b} = {a*b}")
    if islem =="/":
        return(f"{a} / {b} = {a/b}")
    
print("Program Başlatıldı.")
while True:
    try:
        islem = input("İşleminizi seçiniz +-*/: ")
        if islem not in "+-*/":
            print("Lütfen şu işlemlerden birini seçiniz: +-*/")
            continue
        a= int(input("ilk sayıyı giriniz: "))
        b= int(input("ikinici sayıyı giriniz: "))
        print(hesapla(a,b,islem))
        kapat=input("Kapatmak için -1 tuşuna basınız: ")
        if kapat=='-1':
            break
    except:
        print("Lütfen sayıları düzgün giriniz!")


# In[190]:


## Hataları Ele Alma try except tekniği


# In[ ]:




