#!/usr/bin/env python
# coding: utf-8

# In[8]:


nama = input("Masukkan nama: ") #mendeklarasikan input
jumlah = 0 #membuat variabel jumlah = 0

for huruf in nama: #Melakukan iterasi pada setiap huruf dalam variabel
    if huruf.isalpha(): #memeriksa huruf dalam variabel nama berupa alphabet
        jumlah += 1 #menambahkan 1 untuk setiap bertemu dengan huruf alphabet

print("Jumlah huruf dalam nama", nama, "adalah", jumlah) #mencetak jumlah yang ada di variabel


# In[11]:


nama = input("Masukkan nama: ") #mendeklarasikan input
vokal = "aiueoAIUEO" #mendeklarasikan variabel string huruf vokal kecil dan kapital
jumlah = 0 #variabel jumlah dan menginisialisasikannya dengan nilai 0

for huruf in nama: #iterasi pada setiap huruf dalam variabel
    if huruf in vokal: #memeriksa apakah setiap huruf terdapat vokal
        jumlah += 1 #Menambahkan 1 ke variabel jumlah saat bertemu dengan huruf vokal

print("Jumlah huruf vokal dalam nama", nama, "adalah", jumlah) #mencetak hasil perhitungn huruf vokal


# In[12]:


nama = input("Masukkan nama: ") #mendeklarasikan input
konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" #mendeklarasikan variabel string huruf konsonan kecil dan kapital
jumlah = 0 #variabel jumlah dan menginisialisasikannya dengan nilai 0

for huruf in nama: #iterasi pada setiap huruf dalam variabel
    if huruf in konsonan: #memeriksa apakah setiap huruf terdapat konsonan
        jumlah += 1 #Menambahkan 1 ke variabel jumlah saat bertemu dengan huruf konsonan

print("Jumlah huruf konsonan dalam nama", nama, "adalah", jumlah) #mencetak hasil perhitungn huruf konsonan


# In[ ]:




