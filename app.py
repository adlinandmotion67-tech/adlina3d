import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Pengaturan halaman aplikasi
st.set_page_config(
    page_title="AAS Shimadzu AA-7000 Virtual Lab",
    page_icon="🧪",
    layout="wide"
)

# Sidebar Navigasi
st.sidebar.title("AA-7000 Virtual Lab")
st.sidebar.write("Modul Pembelajaran Spektrofotometri")
menu = st.sidebar.radio(
    "Pilih Modul:",
    [
        "Beranda Utama",
        "Teori & Hukum Beer",
        "Preparasi Larutan",
        "Kurva Kalibrasi",
        "Analisis & Validasi"
    ]
)

# ==========================================
# 1. MODUL: BERANDA UTAMA
# ==========================================
if menu == "Beranda Utama":
    st.title("🧪 VIRTUAL LAB AAS")
    st.subheader("Aplikasi Pembelajaran Inklusif & Interaktif Spektrofotometri Serapan Atom (Shimadzu AA-7000)")
    
    st.markdown("""
    Selamat Datang! Aplikasi berbasis web ini dirancang khusus untuk memfasilitasi pembelajaran **Spektrofotometri Serapan Atom (AAS)** secara mendalam, interaktif, dan terstruktur.
    
    #### Fitur Unggulan Simulator Ini:
    *   **Teori Interaktif:** Simulasi langsung Hukum Beer-Lambert dengan grafik dinamis.
    *   **Modul Preparasi:** Kalkulator pengenceran larutan standar & sampel secara cepat.
    *   **Kurva Kalibrasi Dinamis:** Perhitungan regresi linier instan untuk menentukan kelinieran data.
    *   **Validasi Metode:** Analisis presisi (%RSD) dan akurasi (%Recovery) berbasis data laboratorium.
    
    *Tips Penggunaan: Gunakan menu di sidebar kiri untuk berpindah modul secara berurutan.*
    """)

# ==========================================
# 2. MODUL: TEORI & HUKUM BEER
# ==========================================
elif menu == "Teori & Hukum Beer":
    st.title("📚 Teori & Hukum Beer-Lambert")
    st.markdown("""
    ### Prinsip Dasar AAS
    Spektrofotometri Serapan Atom (AAS) adalah metode analisis kuantitatif yang didasarkan pada penyerapan energi cahaya oleh **atom-atom bebas pada keadaan dasar (ground state)**.
    """)
    
    st.latex(r"A = \epsilon \cdot b \cdot C")
    st.caption("A = Absorbansi | ε = Absorptivitas | b = Lebar nyala | C = Konsentrasi")
    
    st.subheader("Simulasi Interaktif")
    col1, col2 = st.columns(2)
    
    with col1:
        epsilon = st.slider("Absorptivitas Molar (ε) [L/(mol.cm)]", min_value=100, max_value=1000, value=500, step=50)
        b = st.slider("Lebar Lintasan / Celah Api (b) [cm]", min_value=1.0, max_value=10.0, value=5.0, step=0.5)
        c = st.slider("Konsentrasi Target (C) x 10⁻⁴ [M]", min_value=0.5, max_value=5.0, value=2.0, step=0.1)
        
        # Hitung Nilai Absorbansi (C dikali 10^-4 untuk simulasi skala kecil)
        absorbansi = epsilon * b * (c * 1e-4)
        st.metric("Nilai Absorbansi (A)", f"{absorbansi:.3f}")
        
    with col2:
        # Menampilkan Grafik Hubungan Konsentrasi dan Absorbansi secara Live
        c_array = np.linspace(0, 6, 100)
        a_array = epsilon * b * (c_array * 1e-4)
        
        fig, ax = plt.subplots()
        ax.plot(c_array, a_array, label='Garis Teoretis', color='blue')
        ax.scatter([c], [absorbansi], color='red', s=100, label='Titik Saat Ini')
        ax.set_xlabel("Konsentrasi (C) x 10⁻⁴ M")
        ax.set_ylabel("Absorbansi (A)")
        ax.set_title("Grafik Hubungan Linier")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

# ==========================================
# 3. MODUL: PREPARASI LARUTAN
# ==========================================
elif menu == "Preparasi Larutan":
    st.title("🧪 Preparasi Larutan & Pengenceran")
    
    st.subheader("Pengenceran Standar (M₁V₁ = M₂V₂)")
    st.write("Hitung volume larutan induk yang perlu dipipet untuk membuat deret standar.")
    
    col1, col2 = st.columns(2)
    with col1:
        m1 = st.number_input("Konsentrasi Larutan Induk (M₁) [ppm]", value=100.0, step=10.0)
        m2 = st.number_input("Kons. Target (M₂) [ppm]", value=5.0, step=0.5)
        v2 = st.number_input("Vol. Labu Takar (V₂) [mL]", value=50.0, step=5.0)
        
        if m1 > 0:
            v1 = (m2 * v2) / m1
            st.success(f"Volume Dipipet (V₁): **{v1:.2f} mL**")
        else:
            st.error("Konsentrasi awal harus lebih besar dari 0")
            
    with col2:
        st.subheader("Faktor Pengenceran (FP) Sampel")
        st.write("Hitung pengali (FP) jika sampel terlalu pekat.")
        v_awal = st.number_input("Volume Pipet Sampel Awal [mL]", value=10.0, step=1.0)
        v_akhir = st.number_input("Ditepatkan dalam Labu Takar [mL]", value=100.0, step=10.0)
        
        if v_awal > 0:
            fp = v_akhir / v_awal
            st.success(f"Faktor Pengenceran (FP): **{fp:.1f} x**")
        else:
            st.error("Volume awal harus lebih besar dari 0")

# ==========================================
# 4. MODUL: KURVA KALIBRASI
# ==========================================
elif menu == "Kurva Kalibrasi":
    st.title("📈 Kurva Kalibrasi Standar")
    st.write("Isi nilai Absorbansi alat berdasarkan deret konsentrasi standar.")
    
    # Input Data Menggunakan Dataframe Interaktif
    data_awal = {
        "Konsentrasi (X) ppm": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
        "Absorbansi (Y)": [0.000, 0.125, 0.252, 0.370, 0.495, 0.615]
    }
    df = pd.DataFrame(data_awal)
    
    edited_df = st.data_editor(df, num_rows="dynamic")
    
    x = edited_df["Konsentrasi (X) ppm"].values
    y = edited_df["Absorbansi (Y)"].values
    
    if len(x) > 1:
        # Perhitungan Regresi Linier Otomatis
        slope, intercept = np.polyfit(x, y, 1)
        r_squared = np.corrcoef(x, y)[0, 1] ** 2
        
        # Simpan nilai slope dan intercept ke dalam session state agar bisa dibaca di halaman lain
        st.session_state['slope'] = slope
        st.session_state['intercept'] = intercept
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Persamaan Regresi")
            st.info(f"**Y = {slope:.4f}X + {intercept:.4f}**")
            st.write(f"**Slope (b):** {slope:.4f}")
            st.write(f"**Intercept (a):** {intercept:.4f}")
            st.write(f"**R² (Linearitas):** {r_squared:.4f}")
            
            # Estimasi Statistik LoD / LoQ Sederhana
            y_pred = slope * x + intercept
            residual_std = np.std(y - y_pred, ddof=2) if len(x) > 2 else 0.001
            lod = (3 * residual_std) / slope if slope != 0 else 0
            loq = (10 * residual_std) / slope if slope != 0 else 0
            
            st.markdown("#### Batas Deteksi")
            st.write(f"**LoD (Batas Deteksi):** {lod:.3f} ppm")
            st.write(f"**LoQ (Batas Kuantitasi):** {loq:.3f} ppm")
            
        with col2:
            fig, ax = plt.subplots()
            ax.scatter(x, y, color='red', label='Data Riil')
            ax.plot(x, y_pred, color='blue', label=f'Trendline (R²={r_squared:.4f})')
            ax.set_xlabel("Konsentrasi (ppm)")
            ax.set_ylabel("Absorbansi (A)")
            ax.set_title("Grafik Kalibrasi")
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)
    else:
        st.warning("Masukkan minimal 2 baris data standar untuk menghitung kurva.")

# ==========================================
# 5. MODUL: ANALISIS & VALIDASI METODE
# ==========================================
elif menu == "Analisis & Validasi":
    st.title("📊 Analisis & Validasi Metode")
    
    # Ambil nilai regresi linier dari halaman Kurva Kalibrasi jika ada
    slope = st.session_state.get('slope', 0.1228)
    intercept = st.session_state.get('intercept', 0.001)
    
    st.markdown(f"**Menggunakan Persamaan Aktif:** `Y = {slope:.4f}X + {intercept:.4f}`")
    
    tab1, tab2, tab3 = st.tabs(["Kadar Sampel", "Uji Presisi (%RSD)", "Uji Akurasi (%Rec)"])
    
    with tab1:
        st.subheader("Hitung Konsentrasi Sampel")
        y_sampel = st.number_input("Absorbansi Alat (Y) untuk Sampel", value=0.350, format="%.3f")
        fp_sampel = st.number_input("Masukkan Faktor Pengenceran (FP)", value=1.0, min_value=1.0)
        
        # Rumus X = (Y - a) / b
        if slope != 0:
            c_hasil = ((y_sampel - intercept) / slope) * fp_sampel
            st.metric("Konsentrasi Akhir Sampel", f"{c_hasil:.3f} ppm")
        else:
            st.error("Kurva kalibrasi tidak valid.")
            
    with tab2:
        st.subheader("Uji Presisi Alat (Keterulangan)")
        st.write("Masukkan nilai absorbansi data replikasi ulangan Anda:")
        
        data_presisi = st.data_editor(
            pd.DataFrame({"Replikasi":, "Absorbansi": [0.350, 0.352, 0.348, 0.351, 0.349]}),
            num_rows="dynamic"
        )
        
        y_vals = data_presisi["Absorbansi"].values
        if len(y_vals) >= 3:
            mean_y = np.mean(y_vals)
            std_y = np.std(y_vals, ddof=1)
            rsd = (std_y / mean_y) * 100
            
            st.write(f"**Rata-rata Absorbansi:** {mean_y:.4f}")
            st.write(f"**Standar Deviasi (SD):** {std_y:.5f}")
            if rsd < 2.0:
                st.success(f"**Relative Standard Deviation (%RSD):** {rsd:.2f}% (Metode Presisi < 2%)")
            else:
                st.warning(f"**Relative Standard Deviation (%RSD):** {rsd:.2f}% (Kurang presisi > 2%)")
        else:
            st.info("Masukkan minimal 3 data ulangan untuk uji presisi.")
            
    with tab3:
        st.subheader("Uji Temu Balik (Metode Spike / Akurasi)")
        c_nol = st.number_input("1. Konsentrasi Sampel Asli (C₀) [ppm]", value=2.0)
        c_add = st.number_input("2. Jumlah Standar Murni yang Ditambahkan (C_add) [ppm]", value=3.0)
        c_satu = st.number_input("3. Konsentrasi Terbaca Setelah Spike (C₁) [ppm]", value=4.9)
        
        if c_add > 0:
            recovery = ((c_satu - c_nol) / c_add) * 100
            st.metric("Persentase Recovery (%Rec)", f"{recovery:.1f} %")
            if 80.0 <= recovery <= 120.0:
