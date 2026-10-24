<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AAS Shimadzu AA-7000 Virtual Lab | Advanced</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://jsdelivr.net" rel="stylesheet">
    <!-- FontAwesome for Icons -->
    <link href="https://cloudflare.com" rel="stylesheet">
    <!-- Chart.js -->
    <script src="https://jsdelivr.net"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
        }
        .sidebar {
            min-height: 100vh;
            background-color: #212529;
            color: #fff;
        }
        .sidebar .nav-link {
            color: #adbcda;
            transition: all 0.3s;
        }
        .sidebar .nav-link:hover, .sidebar .nav-link.active {
            color: #fff;
            background-color: #0d6efd;
            border-radius: 4px;
        }
        .content-section {
            display: none;
        }
        .content-section.active {
            display: block;
        }
        .vlab-screen {
            background-color: #000;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            font-weight: bold;
        }
        .instrument-box {
            border: 2px dashed #ccc;
            border-radius: 8px;
            background: #e9ecef;
            min-height: 350px;
            position: relative;
        }
    </style>
</head>
<body>

<div class="container-fluid">
    <div class="row">
        <!-- SIDEBAR LEFT -->
        <nav class="col-md-3 col-lg-2 d-md-block sidebar collapse p-3">
            <div class="position-sticky">
                <h5 class="text-white border-bottom pb-2 mb-3">
                    <i class="fa-solid fa-flask-vial me-2"></i>AA-7000 Lab
                </h5>
                <ul class="nav flex-column gap-2">
                    <li class="nav-item">
                        <a class="nav-link active" href="#" onclick="switchMenu('beranda', this)">
                            <i class="fa-solid fa-house me-2"></i>Beranda Utama
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="switchMenu('teori', this)">
                            <i class="fa-solid fa-book me-2"></i>Teori & Hukum Beer
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="switchMenu('instrumen', this)">
                            <i class="fa-solid fa-cube me-2"></i>Instrumen 3D
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="switchMenu('preparasi', this)">
                            <i class="fa-solid fa-calculator me-2"></i>Preparasi Larutan
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="switchMenu('kalibrasi', this)">
                            <i class="fa-solid fa-chart-line me-2"></i>Kurva Kalibrasi
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="switchMenu('validasi', this)">
                            <i class="fa-solid fa-square-check me-2"></i>Analisis & Validasi
                        </a>
                    </li>
                </ul>
                <div class="mt-5 pt-5 text-muted small border-top">
                    <p>Versi 3.0 (Advanced HTML)<br>Fokus: Analisis Kimia Kuantitatif</p>
                </div>
            </div>
        </nav>

        <!-- MAIN CONTENT PANEL -->
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 py-4">
            
            <!-- MODUL: BERANDA -->
            <div id="beranda" class="content-section active">
                <div class="p-5 mb-4 bg-light rounded-3 shadow-sm border">
                    <div class="container-fluid py-2">
                        <h1 class="display-5 fw-bold text-primary"><i class="fa-solid fa-desktop me-3"></i>VIRTUAL LAB AAS</h1>
                        <p class="col-md-10 fs-5 text-secondary">Aplikasi Pembelajaran Inklusif & Interaktif Spektrofotometri Serapan Atom (Shimadzu AA-7000)</p>
                    </div>
                </div>

                <div class="row g-4">
                    <div class="col-md-7">
                        <div class="card h-100 shadow-sm">
                            <div class="card-body">
                                <h4 class="card-title text-success"><i class="fa-solid fa-door-open me-2"></i>Selamat Datang!</h4>
                                <p>Aplikasi berbasis web ini dirancang khusus untuk memfasilitasi pembelajaran <strong>Spektrofotometri Serapan Atom (AAS)</strong> secara mendalam, interaktif, dan terstruktur. Modul ini mensimulasikan instrumen nyata dengan pengolahan data analitik aktual.</p>
                                <h5>Fitur Unggulan Simulator Ini:</h5>
                                <ul>
                                    <li><strong>Visualisasi 3D Instrumen:</strong> Jelajahi komponen optik dan proses atomisasi.</li>
                                    <li><strong>Modul Preparasi:</strong> Kalkulator pengenceran larutan standar & sampel.</li>
                                    <li><strong>Kurva Kalibrasi Dinamis:</strong> Perhitungan regresi linier, Limit of Detection (LoD), dan Limit of Quantitation (LoQ).</li>
                                    <li><strong>Validasi Metode:</strong> Analisis presisi (%RSD) dan akurasi (%Recovery).</li>
                                </ul>
                                <div class="alert alert-info mt-3">
                                    <strong><i class="fa-solid fa-circle-info me-2"></i>Tips Penggunaan:</strong> Gunakan menu di sidebar kiri untuk berpindah modul. Disarankan mengikuti urutan dari Teori hingga Validasi.
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-5">
                        <div class="card h-100 shadow-sm bg-dark text-white">
                            <div class="card-body">
                                <h4 class="card-title border-bottom pb-2"><i class="fa-solid fa-users me-2"></i>KELOMPOK 5</h4>
                                <div class="table-responsive">
                                    <table class="table table-dark table-sm table-striped text-white align-middle">
                                        <thead>
                                            <tr>
                                                <th>No</th>
                                                <th>Nama Anggota</th>
                                                <th class="text-end">NIM</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr><td>1</td><td>ADLINA DHIVA TSANIYAH</td><td class="text-end">2560555</td></tr>
                                            <tr><td>2</td><td>ALIIFAH DHIYAAVINA</td><td class="text-end">2560564</td></tr>
                                            <tr><td>3</td><td>ARIF MAULANA</td><td class="text-end">2560579</td></tr>
                                            <tr><td>4</td><td>ELVIA ELVARITTA</td><td class="text-end">2560618</td></tr>
                                            <tr><td>5</td><td>IKE NURCAHYA</td><td class="text-end">2560642</td></tr>
                                            <tr><td>6</td><td>MUHAMMAD ARKAN HANIF</td><td class="text-end">2560676</td></tr>
                                            <tr><td>7</td><td>NABILA PUTRI KHOIRINNISA</td><td class="text-end">2560695</td></tr>
                                            <tr><td>8</td><td>NAILA PUTRI ZAHRA</td><td class="text-end">2560701</td></tr>
                                            <tr><td>9</td><td>RAFI ALIFIA SHARIATI</td><td class="text-end">2560739</td></tr>
                                            <tr><td>10</td><td>NEHA ATSANA PUTRI AHMAD</td><td class="text-end">2460469</td></tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- MODUL: TEORI -->
            <div id="teori" class="content-section">
                <div class="card shadow-sm mb-4">
                    <div class="card-header bg-primary text-white">
                        <h3><i class="fa-solid fa-book-open me-2"></i>Teori & Hukum Beer-Lambert</h3>
                    </div>
                    <div class="card-body">
                        <h5>Prinsip Dasar AAS</h5>
                        <p>Spektrofotometri Serapan Atom (AAS) adalah metode analisis kuantitatif yang didasarkan pada penyerapan energi cahaya oleh <strong>atom-atom bebas pada keadaan dasar (ground state)</strong>. Penyerapan ini sangat spesifik, di mana atom suatu unsur hanya menyerap cahaya pada panjang gelombang resonansinya sendiri (misal Cu pada 324.7 nm).</p>
                        
                        <div class="row mt-4 align-items-center">
                            <div class="col-md-6">
                                <div class="p-4 border rounded bg-light text-center shadow-sm">
