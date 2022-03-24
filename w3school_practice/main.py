print("Merhaba, Dünya!")



## PYTHNO SYNTAX

if 5 > 2:
  print("Beş iki den büyüktür!")

## syntax hatası
""""
if 5 > 2:
print("Beş iki den büyüktür!")
"""

if 5 > 2:
    print("Beş iki den büyüktür!")
if 5 > 2:
        print("Beş iki den büyüktür!")


x = 5
y = "Merhaba, Dünya!"




## PYTHON DEĞİŞKENLER

#Bu bir komut satırıdır
print("Merhaba, Dünya!")


print("Merhaba, Dünya!")#Bu bir komut satırıdır


#print("Merhaba, Dünya!")
print("Şerefe, Dostum!")


#Bu bir komut satırıdır
#sadece bir
#satır yazabilirsiniz
print("Hello, World!")


"""
Bu bir komut satırıdır
birden fazla satır
yazabilirsiniz.
"""
print("Merhaba, Dünya!")





## PYTHON Değişkenler
x = 5
y = "Alperen"
print(x)
print(y)



x = 4       # x şimdi tip int'dir
x = "Alperen" # x şimdi tip string
print(x)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


x = 5
y = "Alperen"
print(type(x))
print(type(y))

x = "Alperen"
# x'i stringe çevirdik.

a = 4
A = "Ayşa"

#üzerine yazdirmaz
benimvar = "Alperen"
benim_var = "Alperen"
_benim_var = "Alperen"
benimVar = "Alperen"
benimVAR = "Alperen"
benimvar2 = "Alperen"


"""
yasak değişken isimleri

2benimvar = "Alperen"
benim-var = "Alperen"
benim var = "Alperen"
"""


BenimDegiskenAdim = "Alperen"

benim_degisken_adim = "Alperen"

print(benim_degisken_adim)

print("")


x, y, z = "Portakal", "Muz", "Çilek"
print(x)
print(y)
print(z)


x = y = z = "Portakal"
print(x)
print(y)
print(z)


fruits = ["elma", "muz", "çilek"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python çok güzeldir"
print(x)


x = "Python"
y = "çok"
z = "güzeldir"
print(x, y)


x = "Python "
y = "çok "
z = "güzeldir"
print(x + y + z)


x = 5
y = 10
print(x + y)

"""
hata verir
x = 5
y = "John"
print(x + y)
"""


print("\nPython - Global Değişkenler")


x = "mükemmel"

def benimfonk():
  print("Python " + x +" dir")

benimfonk()



x = "mükemmel"

def benimfonk():
  x = "fantastik"
  print("Python " + x +" dir")

benimfonk()

print("Python " + x +" dir")


def benimfonk():
  global x
  x = "fantastik"

benimfonk()

print("Python " + x +" dir")


x = "mükemmel"

def benimfonk():
  global x
  x = "fantastik"

benimfonk()

print("Python " + x +" dir")


print("\nPython - Değişken Egzersizleri")

x = 5
print(type(x))
x = "Merhaba Dünya"
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
x = ["elma", "muz", "çilek"]
print(type(x))
x = ("elma", "muz", "çilek")
print(type(x))
x = range(6)
print(type(x))
x = {"isim" : "Alperen", "age" : 36}
print(type(x))
x = {"elma", "muz", "çilek"}
print(type(x))
x = frozenset({"elma", "muz", "çilek"})
print(type(x))
x = True
print(type(x))
x = b"Merhaba"
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = bytearray(5)
print(type(x))

print("\nPython Sayılar")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex


print("\nTip Dönüştürme")
#int'ten float'a çevirme
a = float(x)

#float'tan inte çevirme
b = int(y)

#intten complex'e çevirme
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


print("\nRastgele Sayı")
import random
print(random.randrange(1, 10))


print("\nPython Döküm")
x = int(1)   # x 1 olacaktır
y = int(2.8) # y 2 olacaktır
z = int("3") # z 3 olacaktır


x = float(1)     # x 1.0 olacaktır
y = float(2.8)   # y 2.8 olacaktır
z = float("3")   # z 3.0 olacaktır
w = float("4.2") # w 4.2 olacaktır

x = str("s1") # x 's1' olacaktır
y = str(2)    # y '2' olacaktır
z = str(3.0)  # z '3.0' olacaktır

print("\nPython Strings")
print("Merhaba")
print('Merhaba')
a = "Merhaba"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print("\n"+a)

print("\nDizilerde Stringler")
a = "Merhaba, Dünya!"
print(a[1])

print("")
for x in "muz":
  print(x)

print("\nString Length")
a = "Merhaba, Dünya!"
print(len(a))

print("\Check String")
txt = "Hayattaki en iyi şeyler ücretsizdir!"
print("ücretsiz" in txt)

txt = "Hayattaki en iyi şeyler ücretsizdir!"
if "ücretsiz" in txt:
  print("Evet, 'ücretsiz' mevcuttur.")

print("\nCheck if NOT")
txt = "Hayattaki en iyi şeyler ücretsizdir!"
print("pahalı" not in txt)

txt = "Hayattaki en iyi şeyler ücretsizdir!"
if "pahalı" not in txt:
  print("Hayır, 'pahalı' mevcut değildir.")


print("\nPython - Slicing Strings")
b = "Merhaba, Dünya!"
print(b[2:5])

print("\nSlice From the Start")
b = "Merhaba, Dünya!"
print(b[:5])

print("\nSlice To the End")
b = "Merhaba, Dünya!"
print(b[2:])

print("\nNegative Indexing")
b = "Merhaba, Dünya!"
print(b[-5:-2])

print("\nPython - Modify Strings")
print("\nUpper Case")
a = "Merhaba, Dünya!"
print(a.upper())

print("\nLower Case")
a = "Merhaba, Dünya!"
print(a.lower())

print("\nRemove Whitespace")
a = " Merhaba, Dünya! "
print(a.strip()) # returns "Hello, World!"

print("\nReplace String")
a = "Merhaba, Dünya!"
print(a.replace("H", "J"))

print("\nSplit String")
a = "Merhaba, Dünya!"
print(a.split(",")) # returns ['Hello', ' World!']

print("\nPython - String Concatenation")
print("\nString Concatenation")
a = "Merhaba"
b = "Dünya"
c = a + b
print(c)

a = "Merhaba"
b = "Dünya"
c = a + " " + b
print(c)

print("\nPython - Format - Strings")
print("\nString Format")
age = 36
txt = "Benim adım Alperen, ben " + str(age) +" yaşındayım."
print(txt)