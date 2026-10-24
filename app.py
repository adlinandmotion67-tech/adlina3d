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
            color: #rgba(255,255,255,0.8);
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
        .live-display {
            background: #000;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 1.5rem;
            box-shadow: inset 0 0 10px rgba(0,255,0,0.5);
        }
        .flame {
            width: 30px;
            height: 30px;
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
                    
                    <h4 class="mt-4 fw-bold">Fitur Unggulan Simulator Ini:</h4>
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

            <!-- MODUL 2: TEORI & HUKUM BEER -->
            <div id="menu-teori" class="menu-section d-none">
                <div class="custom-card">
                    <h2 class="fw-bold text-dark">Teori & Hukum Beer-Lambert</h2>
                    <p class="text-secondary">Prinsip dasar Spektrofotometri Serapan Atom berlandaskan pada penyerapan radiasi cahaya oleh atom bebas keadaan dasar.</p>
                    <div class="alert alert-info text-center fs-4 fw-bold">A = ε · b · C</div>
                    
                    <div class="row mt-4">
                        <div class="col-md-5">
                            <label class="form-label fw-bold">Absorptivitas Molar (ε):</label>
                            <input type="range" class="form-range" id="teori-eps" min="100" max="1000" value="500" oninput="updateTeori()">
                            <span id="val-eps">500</span> L/(mol.cm)
                            
                            <label class="form-label fw-bold mt-3">Lebar Lintasan Celah Api (b):</label>
                            <input type="range" class="form-range" id="teori-b" min="1" max="10" value="5" step="0.5" oninput="updateTeori()">
                            <span id="val-b">5.0</span> cm
                            
                            <label class="form-label fw-bold mt-3">Konsentrasi Target (C) x 10⁻⁴:</label>
                            <input type="range" class="form-range" id="teori-c" min="0.5" max="5" value="2" step="0.1" oninput="updateTeori()">
                            <span id="val-c">2.0</span> M
                            
                            <div class="mt-4 p-3 bg-dark text-white rounded text-center">
                                <h5>Nilai Absorbansi (A):</h5>
                                <div id="teori-abs" class="fs-3 fw-bold text-warning">0.500</div>
                            </div>
                        </div>
                        <div class="col-md-7">
                            <canvas id="chartTeori" height="250"></canvas>
                        </div>
                    </div>
                </div>
            </div>

            <!-- MODUL 3: EKSPLORASI INSTRUMEN 3D -->
            <div id="menu-instrumen" class="menu-section d-none">
                <div class="custom-card">
                    <h2 class="fw-bold text-dark">Eksplorasi Instrumen 3D</h2>
