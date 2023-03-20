#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Function untuk menghitung FPB
def hitung_fpb(x, y):
    while(y):
        x, y = y, x % y
    return x

# Function untuk menghitung KPK
def hitung_kpk(x, y):
    kpk = (x*y) / hitung_fpb(x,y)
    return kpk

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print('=== PROGRAM PERHITUNGAN FPB DAN KPK ===')
    print('[1] Hitung FPB')
    print('[2] Hitung KPK')
    print('[3] Keluar')
    print('=======================================')
    print("\n")

# Fungsi untuk memproses pilihan pengguna
def proses_pilihan(pilihan):
    if pilihan == '1':
        angka1 = int(input('Masukkan angka pertama: '))
        angka2 = int(input('Masukkan angka kedua: '))
        fpb = hitung_fpb(angka1, angka2)
        print(f'FPB dari {angka1} dan {angka2} adalah {fpb}')
    elif pilihan == '2':
        angka1 = int(input('Masukkan angka pertama: '))
        angka2 = int(input('Masukkan angka kedua: '))
        kpk = hitung_kpk(angka1, angka2)
        print(f'KPK dari {angka1} dan {angka2} adalah {kpk}')
    elif pilihan == '3':
        print('Terima kasih telah menggunakan program ini!')
    else:
        print('Pilihan tidak valid')
    print("\n")

# Main program
while True:
    tampilkan_menu()
    pilihan = input('Pilihan: ')
    proses_pilihan(pilihan)
    if pilihan == '3':
        break


# In[ ]:




