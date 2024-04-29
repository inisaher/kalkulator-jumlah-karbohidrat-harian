import streamlit as st

# Informasi nama anggota kelompok dan tim
st.sidebar.title('Informasi Tim')
st.sidebar.write('Kelompok 5')
st.sidebar.write('Anggota:')
st.sidebar.write('- Asyahra Mutia Rojak (2320510)')
st.sidebar.write('- Chindy Nur Anjani (2320515)')
st.sidebar.write('- Fadil Zaky As Sammary (2320523) ')
st.sidebar.write('- Mumammad Nur Iqbal (2320537)')
st.sidebar.write('- Rahil Nafisah (2320549)')

# Fungsi untuk menghitung jumlah karbohidrat harian
def hitung_karbohidrat(berat_badan, tinggi_badan, usia):
    karbohidrat_harian = (berat_badan + tinggi_badan) * 2 + (usia / 10)
    return karbohidrat_harian

# Fungsi utama untuk menjalankan aplikasi
def main():
    st.title("Kalkulator Jumlah Karbohidrat Harian")

    st.write("Program ini membantu Anda menentukan jumlah karbohidrat harian berdasarkan beberapa faktor.")

    # Input nama pengguna
    nama = st.text_input("Masukkan nama Anda:")

    # Input usia
    usia = st.number_input("Masukkan usia Anda:", min_value=1, max_value=120)

    # Input berat badan
    berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0)

    # Input tinggi badan
    tinggi_badan = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=1.0)

    # Tombol untuk menghitung
    if st.button("Hitung"):
        # Hitung jumlah karbohidrat harian
        karbohidrat_harian = hitung_karbohidrat(berat_badan, tinggi_badan, usia)
        
        st.success(f"Halo {nama}, jumlah karbohidrat harian yang disarankan adalah: {karbohidrat_harian:.2f} gram")

        # Tambahkan peringatan dan informasi berdasarkan berat badan dan usia
        if berat_badan > 100:
            st.warning("Wow, berat badan Anda cukup tinggi. Pastikan untuk berkonsultasi dengan dokter untuk saran lebih lanjut.")

        if usia > 60:
            st.info("Anda sudah berusia di atas 60 tahun, pastikan untuk mengonsumsi makanan yang kaya nutrisi untuk mendukung kesehatan Anda.")

# Panggil fungsi utama untuk menjalankan aplikasi
main()