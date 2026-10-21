import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Bikin 1000 data acak
np.random.seed(42)
random.seed(42)

kategori_produk = {
    'Elektronik': ['Laptop', 'Smartphone', 'Tablet', 'Monitor PC'],
    'Pendidikan': ['Buku', 'Alat Tulis', 'Tas Ransel', 'Papan Tulis']
}

harga_dasar = {
    'Laptop': 8500000, 'Smartphone': 4200000, 'Tablet': 3500000, 'Monitor PC': 2100000,
    'Buku': 75000, 'Alat Tulis': 25000, 'Tas Ransel': 150000, 'Papan Tulis': 300000
}

data = []
start_date = datetime(2024, 1, 1)

for _ in range(1000):
    kategori = random.choice(list(kategori_produk.keys()))
    produk = random.choice(kategori_produk[kategori])
    harga = round(harga_dasar[produk] * random.uniform(0.9, 1.1), -3)
    
    if kategori == 'Elektronik':
        jumlah = random.randint(5, 50)
    else:
        jumlah = random.randint(20, 150)
        
    tanggal = start_date + timedelta(days=random.randint(0, 364))
    data.append([produk, kategori, int(harga), jumlah, tanggal.strftime('%d/%m/%y')])

df = pd.DataFrame(data, columns=['Produk', 'Kategori', 'Harga (Rp)', 'Jumlah Terjual', 'Tanggal'])
df['Total Pendapatan'] = df['Harga (Rp)'] * df['Jumlah Terjual']
df.to_csv('dataset_penjualan_1000.csv', index=False)
print("Data berhasil dibikin cuy! Lanjut buka app.py")