import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Penjualan", page_icon="📊", layout="wide")

# NAMA LU UDAH DITAMBAHIN DI SINI YAA 👇
st.title("📊 Dashboard Bedah Kasus 1 - Raffi Kurniawan (241041001)")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('dataset_penjualan_1000.csv')
    df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='%d/%m/%y')
    df['Bulan'] = df['Tanggal'].dt.to_period('M').astype(str)
    return df

df = load_data()

# Tampilkan Angka Total
col1, col2, col3 = st.columns(3)
col1.metric("Total Pendapatan", f"Rp {df['Total Pendapatan'].sum():,.0f}".replace(',', '.'))
col2.metric("Total Barang Terjual", f"{df['Jumlah Terjual'].sum():,}".replace(',', '.'))
col3.metric("Total Transaksi", f"{len(df)}")
st.divider()

# Grafik Baris 1
col_a, col_b = st.columns(2)
with col_a:
    st.subheader("Tren Penjualan (Waktu - Interval)")
    tren = df.groupby('Bulan')['Total Pendapatan'].sum().reset_index()
    st.plotly_chart(px.line(tren, x='Bulan', y='Total Pendapatan', markers=True), use_container_width=True)

with col_b:
    st.subheader("Distribusi Harga (Numerik Kontinu)")
    st.plotly_chart(px.histogram(df, x='Harga (Rp)', color='Kategori', nbins=20), use_container_width=True)

# Grafik Baris 2
col_c, col_d = st.columns(2)
with col_c:
    st.subheader("Penjualan per Produk (Kategorik Nominal)")
    prod_sales = df.groupby('Produk')['Jumlah Terjual'].sum().reset_index().sort_values('Jumlah Terjual')
    st.plotly_chart(px.bar(prod_sales, x='Jumlah Terjual', y='Produk', orientation='h'), use_container_width=True)

with col_d:
    st.subheader("Proporsi Kategori (Kategorik Nominal)")
    kat_prop = df.groupby('Kategori')['Total Pendapatan'].sum().reset_index()
    st.plotly_chart(px.pie(kat_prop, values='Total Pendapatan', names='Kategori', hole=0.4), use_container_width=True)

# Tabel Data
st.subheader("Tabel Dataset Mentah")
st.dataframe(df, use_container_width=True)