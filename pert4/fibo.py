#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("masukkan panjang deret: ")) #mendeklarasikan untuk input

for i in range(n): #awal perulangan for untuk i
    angka1=0 #deklarasi nilai pertama
    angka2=1 #deklarasi nilai kedua
    for j in range(i+1): #perulangan for dengan range increment / pertambahan
        print(angka1, end=' ') #cetak nilai pertama dan ditambahkan spasi
        angka3=angka1+angka2 #deklarasi nilai ketiga yang berisi nilai pertama ditambah nilai kedua
        angka1=angka2 #nilai pertama sama dengan nilai kedua
        angka2=angka3 #nilai kedua sama dengan nilai ketiga
    print() #cetak semua hal yang sudah dilakukan


# In[ ]:




