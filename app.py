# Import Core PKGS
import streamlit as st

# Import Fungsi Belaok
from bela_dash import run_bela_dash
#from bela_top import run_bela_top

def main():
    st.title("Dashboard BelaOK Provinsi Kalimantan Barat")

    menu = ["Home", "Dashboard BelaOK", "TOP 10"]
    pilih = st.selectbox("Pilihan Menu", menu)

    if pilih == "Home":
        st.subheader("Tentang BelaOK")
        st.write("Belanja Langsung Online Kalbar yang disingkat BelaOK adalah upaya Pemerintah Provinsi Kalimantan Barat dalam mewujudkan prinsip-prinsip Pengadaan Barang/Jasa Pemerintah yang efisien, efektif, transparan, akuntabel, adil, tidak diskriminatif dengan cara digitalisasi proses Pengadaan Barang/Jasa dengan mengoptimalkan pemanfaatan Toko Daring sebagai upaya peningkatan peran serta Pelaku UMK di Provinsi Kalimantan Barat.")
        st.write("Program untuk mendukung Program Usaha Mikro dan Kecil (UMK) Go Digital melalui proses Belanja Langsung K/L/PD yang bernilai paling tinggi Rp. 200.000.000,00 (Dua Ratus Juta Rupiah) kepada UMK yang tergabung dalam BelaOK. Program ini merupakan Dukungan Pemerintah Provinsi Kalimantan Barat, sebagai bagian dari Gerakan Bangga Buatan Indonesia sebagai upaya untuk menanggulangi dampak COVID-19 terhadap kegiatan perekonomian, khususnya bagi Usaha Mikro dan Usaha Kecil di Provinsi Kalimantan Barat")
    elif pilih == "Dashboard BelaOK":
        #st.subheader("Dashboard BelaOK")
        run_bela_dash()
    else:
        st.subheader("Isinya Lagi Dipikirkan")
        st.write("Isinya Lagi Dipikirkan")
        # run_bela_top()

if __name__ == '__main__':
    main()