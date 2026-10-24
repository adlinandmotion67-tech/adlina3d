import streamlit as st
import streamlit.components.v1 as components

# Set konfigurasi halaman agar penuh ke samping (Wide mode)
st.set_page_config(
    page_title="AAS Shimadzu AA-7000 Virtual Lab",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Seluruh kode visual mewah asli (HTML, CSS, dan JavaScript interaktif)
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AAS Shimadzu AA-7000 Virtual Lab</title>
    <!-- Tailwind CSS untuk Desain Dashboard Modern -->
    <script src="https://jsdelivr.net"></script>
    <!-- Chart.js untuk Grafik Dinamis Interaktif -->
    <script src="https://jsdelivr.net"></script>
    <!-- Lucide Icons untuk Ikon Menu -->
    <script src="https://unpkg.com"></script>
    <style>
        @import url('https://googleapis.com');
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #0f172a; color: #f8fafc; }
        .sidebar-item.active { background-color: #1e293b; color: #38bdf8; border-left: 4px solid #38bdf8; }
        input[type="range"] { accent-color: #38bdf8; }
    </style>
</head>
<body class="flex h-screen overflow-hidden">

    <!-- SIDEBAR NAVIGASI KIRI -->
    <div class="w-64 bg-slate-900 border-r border-slate-800 flex flex-col justify-between">
        <div>
            <div class="p-6 border-b border-slate-800 flex items-center gap-3">
                <div class="bg-sky-500/20 p-2 rounded-lg text-sky-400">
                    <i data-lucide="beaker" class="w-6 h-6"></i>
                </div>
                <div>
                    <h1 class="font-bold text-sm text-slate-200 tracking-wide">AA-7000 Lab</h1>
                    <p class="text-xs text-sky-400 font-medium">Versi 3.0 Advanced</p>
                </div>
            </div>
            <nav class="mt-6 px-3 space-y-1">
                <button onclick="switchTab('beranda')" id="menu-beranda" class="sidebar-item active w-full flex items-center gap-3 px-4 py-3 text-sm font-medium text-slate-400 rounded-lg hover:bg-slate-800/50 hover:text-slate-200 transition">
                    <i data-lucide="home" class="w-4 h-4"></i> Beranda Utama
                </button>
                <button onclick="switchTab('teori')" id="menu-teori" class="sidebar-item w-full flex items-center gap-3 px-4 py-3 text-sm font-medium text-slate-400 rounded-lg hover:bg-slate-800/50 hover:text-slate-200 transition">
                    <i data-lucide="book-open" class="w-4 h-4"></i> Teori & Hukum Beer
                </button>
                <button onclick="switchTab('instrumen')" id="menu-instrumen" class="sidebar-item w-full flex items-center gap-3 px-4 py-3 text-sm font-medium text-slate-400 rounded-lg hover:bg-slate-800/50 hover:text-slate-200 transition">
                    <i data-lucide="layers" class="w-4 h-4"></i> Instrumen 3D
                </button>
                <div class="px-4 py-2 text-xs font-semibold text-slate-500 uppercase tracking-wider mt-4">Modul Analitik</div>
                <button onclick="switchTab('preparasi')" id="menu-preparasi" class="sidebar-item w-full flex items-center gap-3 px-4 py-3 text-sm font-medium text-slate-400 rounded-lg hover:bg-slate-800/50 hover:text-slate-200 transition">
                    <i data-lucide="calculator" class="w-4 h-4"></i> Preparasi Larutan
                </button>
                <button onclick="switchTab('kurva')" id="menu-kurva" class="sidebar-item w-full flex items-center gap-3 px-4 py-3 text-sm font-medium text-slate-400 rounded-lg hover:bg-slate-800/50 hover:text-slate-200 transition">
                    <i data-lucide="trending-up" class="w-4 h-4"></i> Kurva Kalibrasi
                </button>
                <button onclick="switchTab('validasi')" id="menu-validasi" class="sidebar-item w-full flex items-center gap-3 px-4 py-3 text-sm font-medium text-slate-400 rounded-lg hover:bg-slate-800/50 hover:text-slate-200 transition">
                    <i data-lucide="check-square" class="w-4 h-4"></i> Analisis & Validasi
                </button>
            </nav>
        </div>
        <div class="p-4 border-t border-slate-800 text-xs text-slate-500 text-center">
            Fokus: Analisis Kimia Kuantitatif
        </div>
    </div>

    <!-- AREA KONTEN UTAMA -->
    <div class="flex-1 overflow-y-auto bg-slate-950 p-8">
        
        <!-- ================= BERANDA UTAMA ================= -->
        <div id="tab-beranda" class="tab-content space-y-6">
            <div class="bg-gradient-to-r from-sky-900/40 to-slate-900 p-8 rounded-2xl border border-sky-500/20 shadow-xl">
                <span class="bg-sky-500/10 text-sky-400 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider">Selamat Datang</span>
                <h2 class="text-3xl font-extrabold text-white mt-3">VIRTUAL LAB AAS SHIMADZU AA-7000</h2>
                <p class="text-slate-400 mt-2 max-w-3xl text-sm leading-relaxed">
                    Aplikasi pembelajaran inklusif dan interaktif ini mensimulasikan operasional instrumen nyata laboratorium dengan pengolahan data analitik aktual spektrofotometri serapan atom.
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="bg-slate-900/60 p-5 rounded-xl border border-slate-800/80">
                    <div class="text-sky-400 mb-3"><i data-lucide="eye" class="w-6 h-6"></i></div>
                    <h3 class="font-semibold text-sm text-slate-200">Visualisasi 3D</h3>
                    <p class="text-xs text-slate-500 mt-1">Eksplorasi struktur optik internal dan ruang pembakaran atomisasi nyala api.</p>
                </div>
                <div class="bg-slate-900/60 p-5 rounded-xl border border-slate-800/80">
                    <div class="text-emerald-400 mb-3"><i data-lucide="flask-conical" class="w-6 h-6"></i></div>
                    <h3 class="font-semibold text-sm text-slate-200">Modul Preparasi</h3>
                    <p class="text-xs text-slate-500 mt-1">Simulasi kalkulator pengenceran deret larutan induk standar laboratorium.</p>
                </div>
                <div class="bg-slate-900/60 p-5 rounded-xl border border-slate-800/80">
                    <div class="text-amber-400 mb-3"><i data-lucide="line-chart" class="w-6 h-6"></i></div>
                    <h3 class="font-semibold text-sm text-slate-200">Kurva Kalibrasi</h3>
                    <p class="text-xs text-slate-500 mt-1">Algoritma perhitungan otomatis regresi linier, batas deteksi LoD & LoQ.</p>
                </div>
                <div class="bg-slate-900/60 p-5 rounded-xl border border-slate-800/80">
                    <div class="text-indigo-400 mb-3"><i data-lucide="shield-check" class="w-6 h-6"></i></div>
                    <h3 class="font-semibold text-sm text-slate-200">Validasi Metode</h3>
                    <p class="text-xs text-slate-500 mt-1">Evaluasi tingkat kedekatan presisi (%RSD) dan akurasi temu balik (%Recovery).</p>
                </div>
            </div>
        </div>

        <!-- ================= TEORI & HUKUM BEER ================= -->
        <div id="tab-teori" class="tab-content hidden space-y-6">
            <h2 class="text-2xl font-bold text-white flex items-center gap-2"><i data-lucide="book-open" class="text-sky-400"></i> Teori & Hukum Beer-Lambert</h2>
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 space-y-4">
                    <h3 class="font-semibold text-slate-200 border-b border-slate-800 pb-2">Parameter Simulasi</h3>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">Absorptivitas Molar (ε): <span id="val-eps" class="text-sky-400 font-bold">500</span></label>
                        <input type="range" id="input-eps" min="100" max="1000" value="500" step="50" oninput="simulasiBeer()" class="w-full h-1 bg-slate-800 rounded-lg appearance-none cursor-pointer">
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">Lebar Jalur Celah Api (b): <span id="val-b" class="text-sky-400 font-bold">5.0</span> cm</label>
                        <input type="range" id="input-b" min="1" max="10" value="5" step="0.5" oninput="simulasiBeer()" class="w-full h-1 bg-slate-800 rounded-lg appearance-none cursor-pointer">
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">Konsentrasi Target (C) x 10⁻⁴: <span id="val-c" class="text-sky-400 font-bold">2.0</span> M</label>
                        <input type="range" id="input-c" min="0.5" max="5" value="2" step="0.1" oninput="simulasiBeer()" class="w-full h-1 bg-slate-800 rounded-lg appearance-none cursor-pointer">
                    </div>
                    <div class="bg-slate-950 p-4 rounded-lg border border-slate-800/80 text-center">
                        <div class="text-xs text-slate-400 font-medium">Output Nilai Absorbansi (A)</div>
                        <div id="output-beer-a" class="text-3xl font-black text-sky-400 mt-1">0.500</div>
                    </div>
                </div>
                <div class="lg:col-span-2 bg-slate-900 p-6 rounded-xl border border-slate-800 flex items-center justify-center">
                    <div class="w-full h-64"><canvas id="beerChart"></canvas></div>
                </div>
            </div>
        </div>

        <!-- ================= INSTRUMEN 3D SIMULATOR ================= -->
        <div id="tab-instrumen" class="tab-content hidden space-y-6">
            <div class="flex justify-between items-center">
