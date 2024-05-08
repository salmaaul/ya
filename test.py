import streamlit as st 

def konfigurasi_elektron(atomic_number):
    # Dictionary untuk menyimpan jumlah elektron di setiap kulit
    electron_config = {'1': '1s¹', '2': '1s²', '3': '2s¹ 2p¹', '4': '2s² 2p²', '5': '2s² 2p³',
                       '6': '2s² 2p⁴', '7': '2s² 2p⁵', '8': '2s² 2p⁶', '9': '2s² 2p⁶ 3s¹',
                       '10': '2s² 2p⁶ 3s²', '11': '2s² 2p⁶ 3s² 3p¹', '12': '2s² 2p⁶ 3s² 3p²',
                       '13': '2s² 2p⁶ 3s² 3p³', '14': '2s² 2p⁶ 3s² 3p⁴', '15': '2s² 2p⁶ 3s² 3p⁵',
                       '16': '2s² 2p⁶ 3s² 3p⁶', '17': '2s² 2p⁶ 3s² 3p⁶ 4s¹', '18': '2s² 2p⁶ 3s² 3p⁶ 4s²'}

    # Mengecek apakah nomor atom valid
    if atomic_number not in electron_config:
        return "Nomor atom tidak valid. Masukkan nomor atom antara 1 hingga 18."

    return electron_config[atomic_number]

def main():
    st.title("Aplikasi Konfigurasi Elektron")
    st.write("Aplikasi ini menghasilkan konfigurasi elektron untuk atom dengan nomor atom tertentu.")

    # Membuat input untuk nomor atom
    atomic_number = st.text_input("Masukkan nomor atom (1-18):")

