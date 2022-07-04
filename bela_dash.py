import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency

def run_bela_dash():
    # Page Setting
    #st.set_page_config(layout="wide")

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Dataset
    df = pd.read_excel("data/belaok_mentah_4072022.xlsx", sheet_name="list_po")
    dfsku = pd.read_excel("data/belaok_mentah_4072022.xlsx", sheet_name="list_sku")
    dfv = pd.read_excel("data/belaok_mentah_4072022.xlsx", sheet_name="list_vendor")

    df['bulan'] = pd.to_datetime(df['po_created_at']).dt.month

    # Olah data Jumlah Produk, Jumlah Transaksi dan Jumlah Vendor
    sku = dfsku.shape
    transaksi = df.shape
    vendor = dfv.shape

    # Olah data Nilai PO Created, PO Delivered dan PO Close
    po_created = format_currency(df['total'].sum(), 'Rp. ', locale='id_ID')    
    po_delivered = df[(df['status_po'] == "PO Delivered")]
    po_close = df[(df['status_po'] == "PO Close")]

    # Olah data Nilai Pajak Daerah, PPN dan PPH
    po_pd = po_close['pajak_daerah'].sum()
    po_ppn = po_close['ppn'].sum()
    po_pph = po_close['pph'].sum()

    df10b = po_delivered.buyer.value_counts().sort_values(ascending=False).head(10)
    df10bnilai = po_delivered.groupby(by='buyer').sum().sort_values(by='sub_total',ascending=False)['sub_total'].head(10)
    df10s = po_delivered.seller.value_counts().sort_values(ascending=False).head(10)
    df10snilai = po_delivered.groupby(by='seller').sum().sort_values(by='sub_total',ascending=False)['sub_total'].head(10)

    # Row Jumlah Produk, Transaksi dan Vendor
    a1, a2, a3 = st.columns(3)
    a1.metric("Jumlah Produk", '{:,}'.format(sku[0]))
    a2.metric("Jumlah Transaksi", '{:,}'.format(transaksi[0]))
    a3.metric("Jumlah Vendor", '{:,}'.format(vendor[0]))

    # Row Nilai PO Created, PO Delivered dan PO Close
    b1, b2, b3 = st.columns(3)
    b1.metric("PO Created", po_created)
    b2.metric("PO Delivered", format_currency(po_delivered['sub_total'].sum(), 'Rp. ', locale='id_ID'))
    b3.metric("PO Close", format_currency(po_close['sub_total'].sum(), 'Rp. ', locale='id_ID'))
    
    # Row Nilai Pajak Daerah, PPN dan PPH
    c1, c2, c3 = st.columns(3)
    c1.metric("Pajak Daerah", format_currency(po_pd, 'Rp. ', locale='id_ID'))
    c2.metric("PPN PKP", format_currency(po_ppn, 'Rp. ', locale='id_ID'))
    c3.metric("PPH 22 dan PPH 23", format_currency(po_pph, 'Rp. ', locale='id_ID'))

    # Row Top 10 OPD Transaksi Terbanyak
    d1, d2 = st.columns((5,5))
    with d1:
        st.markdown('### Top 10 OPD Jumlah Transaksi')
        st.dataframe(df10b)

    with d2:
        st.markdown('### Top 10 OPD Jumlah Transaksi Chart')
        fig10b = plt.figure(figsize=(20,13))
        sns.barplot(x=df10b, y=df10b.index)
        st.pyplot(fig10b)
        
    # Row Top 10 OPD Nilai Transaksi Terbanyak
    e1, e2 = st.columns((5,5))
    with e1:
        st.markdown('### Top 10 OPD Nilai Transaksi')
        st.dataframe(df10bnilai)        
    
    with e2:
        st.markdown('### Top 10 OPD Nilai Transaksi Chart')
        fig10bnilai = plt.figure(figsize=(20,13))
        sns.barplot(x=df10bnilai, y=df10bnilai.index)
        st.pyplot(fig10bnilai)

    # Row Top 10 Seller Jumlah Transaksi Terbanyak
    f1, f2 = st.columns((5,5))
    with f1:
        st.markdown('### Top 10 Seller Jumlah Transaksi')
        st.dataframe(df10s)        
    
    with f2:
        st.markdown('### Top 10 OPD Jumlah Transaksi Chart')
        fig10s = plt.figure(figsize=(20,13))
        sns.barplot(x=df10s, y=df10s.index)
        st.pyplot(fig10s)        

    # Row Top 10 Seller Nilai Transaksi Terbanyak
    g1, g2 = st.columns((5,5))
    with g1:
        st.markdown('### Top 10 Seller Nilai Transaksi')
        st.dataframe(df10snilai)        
    
    with g2:
        st.markdown('### Top 10 OPD Nilai Transaksi Chart')
        fig10snilai = plt.figure(figsize=(20,13))
        sns.barplot(x=df10snilai, y=df10snilai.index)
        st.pyplot(fig10snilai)        


"""
    # Row C
    g1, g2 = st.columns((5,5))
    with g1:
        st.markdown('### Heatmap')
        plost.time_hist(
            data=seattle_weather,
            date='date',
            x_unit='week',
            y_unit='day',
            color='temp_max',
            aggregate='median',
            legend=None)
    with g2:
        st.markdown('### Bar chart')
        plost.donut_chart(
            data=stocks,
            theta='q2',
            color='company')
"""

