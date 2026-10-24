import streamlit as st
import streamlit.components.v1 as components

# Mengatur tampilan halaman utama menjadi wide (lebar)
st.set_page_config(
    page_title="AAS Shimadzu AA-7000 Virtual Lab",
    page_icon="🧪",
    layout="wide"
)

# Seluruh aplikasi HTML, CSS Modern, dan JavaScript interaktif dibungkus di sini dengan aman
html_lab_aplikasi = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AAS Shimadzu AA-7000 Virtual Lab</title>
    <!-- Bootstrap & FontAwesome untuk tampilan modern ala Dashboard Lab -->
    <link href="https://jsdelivr.net" rel="stylesheet">
    <link href="https://cloudflare.com" rel="stylesheet">
    <!-- Chart.js untuk Grafik Dinamis yang Bisa Diklik dan Digeser -->
    <script src="https://jsdelivr.net"></script>
    
    <style>
        :root {
            --primary-color: #2c3e50;
            --accent-color: #00adb5;
            --dark-bg: #1a1a2e;
            --card-bg: #222831;
            --text-light: #eeeeee;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
            color: #333;
        }
        .sidebar {
            background-color: var(--primary-color);
            color: white;
            min-height: 100vh;
            padding-top: 20px;
        }
        .sidebar .nav-link {
            color: rgba(255,255,255,0.8);
            margin: 5px 15px;
            padding: 12px;
            border-radius: 8px;
            transition: all 0.3s;
        }
        .sidebar .nav-link:hover, .sidebar .nav-link.active {
            background-color: var(--accent-color);
            color: white;
            font-weight: bold;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .main-content {
            padding: 30px;
        }
        .custom-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            padding: 25px;
            margin-bottom: 25px;
            border-left: 5px solid var(--accent-color);
        }
        .visual-3d-box {
            background-color: var(--dark-bg);
            color: var(--text-light);
            border-radius: 12px;
            height: 400px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
            border: 2px dashed var(--accent-color);
        }
        .flame {
            width: 35px;
            height: 35px;
            background: linear-gradient(transparent, #ff3d00, #ffea00);
            border-radius: 0 50% 50% 50%;
            transform: rotate(-45deg);
            animation: burn 0.5s infinite alternate;
            display: none;
        }
        @keyframes burn {
            from { transform: rotate(-45deg) scale(0.9); }
            to { transform: rotate(-45deg) scale(1.1); }
        }
    </style>
</head>
<body>

<div class="container-fluid">
    <div class="row">
        <!-- SIDEBAR MENU MODIS -->
        <nav class="col-md-3 col-lg-2 d-md-block sidebar collapse shadow">
            <div class="position-sticky text-center mb-4">
                <i class="fa-solid fa-flask-vial fa-3x text-info mb-2"></i>
                <h5 class="fw-bold">AA-7000 Lab</h5>
                <span class="badge bg-secondary">Versi 3.0 Advanced</span>
            </div>
            <ul class="nav flex-column">
                <li class="nav-item">
                    <a class="nav-link active" href="#" onclick="switchMenu('beranda', this)"><i class="fa-solid fa-house me-2"></i> Beranda Utama</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" onclick="switchMenu('teori', this)"><i class="fa-solid fa-book-open me-2"></i> Teori & Hukum Beer</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" onclick="switchMenu('instrumen', this)"><i class="fa-solid fa-cube me-2"></i> Instrumen 3D</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" onclick="switchMenu('preparasi', this)"><i class="fa-solid fa-calculator me-2"></i> Preparasi Larutan</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" onclick="switchMenu('kalibrasi', this)"><i class="fa-solid fa-chart-line me-2"></i> Kurva Kalibrasi</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#" onclick="switchMenu('validasi', this)"><i class="fa-solid fa-square-check me-2"></i> Analisis & Validasi</a>
                </li>
            </ul>
        </nav>

        <!-- MAIN INTERACTIVE CONTENT -->
        <main class="col-md-9 ms-sm-auto col-lg-10 main-content">
            
            <!-- MODUL 1: BERANDA -->
            <div id="menu-beranda" class="menu-section">
                <div class="custom-card">
                    <h1 class="display-5 fw-bold text-dark"><i class="fa-solid fa-atom text-info"></i> VIRTUAL LAB AAS</h1>
                    <p class="lead text-secondary">Aplikasi Pembelajaran Inklusif & Interaktif Spektrofotometri Serapan Atom (Shimadzu AA-7000)</p>
                    <hr>
                    <p>Selamat Datang! Aplikasi berbasis web ini dirancang khusus untuk memfasilitasi pembelajaran laboratorium instrumen secara mendalam, interaktif, dan terstruktur. Modul ini mensimulasikan instrumen nyata dengan pengolahan data analitik aktual.</p>
                    
                    <!-- TABEL KELOMPOK 5 YANG DIINGINKAN -->
                    <div class="mt-4">
                        <h5 class="fw-bold text-dark mb-3"><i class="fa-solid fa-users text-primary"></i> IDENTITAS KELOMPOK 5</h5>
                        <table class="table table-bordered table-striped table-hover text-center align-middle shadow-sm">
                            <thead class="table-dark">
                                <tr>
                                    <th style="width: 10%;">No</th>
                                    <th>Nama Anggota</th>
                                    <th style="width: 25%;">NIM</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td>1</td><td>ADLINA DHIVA TSANIYAH</td><td>2560555</td></tr>
                                <tr><td>2</td><td>ALIIFAH DHIYAAVINA</td><td>2560564</td></tr>
                                <tr><td>3</td><td>ARIF MAULANA</td><td>2560579</td></tr>
                                <tr><td>4</td><td>ELVIA ELVARITTA</td><td>2560618</td></tr>
                                <tr><td>5</td><td>IKE NURCAHYA</td><td>2560642</td></tr>
                                <tr><td>6</td><td>MUHAMMAD ARKAN HANIF</td><td>2560676</td></tr>
                                <tr><td>7</td><td>NABILA PUTRI KHOIRINNISA</td><td>2560695</td></tr>
                                <tr><td>8</td><td>NAILA PUTRI ZAHRA</td><td>2560701</td></tr>
                                <tr><td>9</td><td>RAFI ALIFIA SHARIATI</td><td>2560739</td></tr>
                                <tr><td>10</td><td>NEHA ATSANA PUTRI AHMAD</td><td>2460469</td></tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <h4 class="mt-4 fw-bold">Fitur Utama Simulator Ini:</h4>
                    <div class="row mt-3">
                        <div class="col-md-6 mb-3">
                            <div class="p-3 bg-light rounded shadow-sm"><i class="fa-solid fa-vr-cardboard text-success me-2"></i> <strong>Visualisasi 3D Instrumen:</strong> Jelajahi komponen optik dan proses atomisasi.</div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="p-3 bg-light rounded shadow-sm"><i class="fa-solid fa-vial text-warning me-2"></i> <strong>Modul Preparasi:</strong> Kalkulator pengenceran larutan standar & sampel instan.</div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="p-3 bg-light rounded shadow-sm"><i class="fa-solid fa-chart-simple text-danger me-2"></i> <strong>Kurva Kalibrasi Dinamis:</strong> Perhitungan regresi linier nyata beserta penentuan nilai LoD & LoQ.</div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="p-3 bg-light rounded shadow-sm"><i class="fa-solid fa-check-double text-primary me-2"></i> <strong>Validasi Metode:</strong> Analisis presisi (%RSD) dan akurasi (%Recovery).</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- MODUL 2: TEORI -->
            <div id="menu-teori" class="menu-section d-none">
                <div class="custom-card">
                    <h2 class="fw-bold text-dark">Teori & Hukum Beer-Lambert</h2>
                    <p class="text-secondary">Prinsip dasar Spektrofotometri Serapan Atom berlandaskan pada penyerapan radiasi cahaya oleh atom bebas keadaan dasar.</p>
                    <div class="alert alert-info text-center fs-4 fw-bold">A = ε · b · C</div>
                    
                    <div class="row mt-4">
                        <div class="col-md-5">
                            <label class="form-label fw-bold">Absorptivitas Molar (ε):</label>
                            <input type="range" class="form-range" id="teori-eps" min="100" max="1000" value="500" oninput="updateTeori()">
