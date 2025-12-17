# 🌍 NetCarbon Tracker
**CLI-Based Server Live Monitoring & Carbon Emission Estimation**

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/status-Final%20Release-success?style=for-the-badge)
![License](https://img.shields.io/badge/license-Educational%20Use-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)

---

## 📖 Deskripsi Singkat
**NetCarbon Tracker** adalah aplikasi berbasis Command Line Interface (CLI) yang dikembangkan menggunakan Python untuk memantau kinerja server Linux (CPU Load & RAM Usage) secara *live* melalui protokol SSH. Lebih dari sekadar alat monitoring, aplikasi ini berfokus pada **Green Computing** dengan mengonversi penggunaan sumber daya server menjadi estimasi **emisi karbon (CO₂)** secara *real-time*.

Proyek ini mendukung pencapaian **Sustainable Development Goals (SDGs)**:
* **SDG 9:** Industri, Inovasi, dan Infrastruktur
* **SDG 12:** Konsumsi dan Produksi yang Bertanggung Jawab
* **SDG 13:** Penanganan Perubahan Iklim

---

## 🚀 Evolusi Versi
Proyek ini dikembangkan dalam tiga tahap iterasi:

### 🔹 [v1.0 - Alpha Release](./v1_alpha)
* **Fokus:** *Proof of Concept* (PoC).
* **Fitur:** Koneksi SSH dasar ke 3 server, pengambilan data CPU/RAM mentah.
* **Tampilan:** CLI standar tanpa warna.

### 🔹 [v2.0 - Beta Release](./v2_beta)
* **Fokus:** Penambahan kalkulasi energi.
* **Fitur:** Menghitung estimasi Watt & CO₂ dengan koefisien studi kasus 5.333 server.
* **Tampilan:** Indikator **Bicolor** (Hijau/Merah) untuk status emisi sederhana.

### 🏆 [v3.0 - Final Release](./v3_final) *(Recommended)*
* **Fokus:** Stabilitas, Visualisasi, dan Agregasi Data.
* **Fitur:**
    * **Live Monitoring** interval 2 detik.
    * **Tricolor Output System** (Hijau/Kuning/Merah) berbasis *threshold*.
    * **Data Aggregation:** Menghitung rata-rata emisi per menit.
    * Koefisien studi kasus ditingkatkan ke **6.400** server.

---


## ⚙️ Persyaratan Sistem
Untuk menjalankan versi final, pastikan lingkungan Anda memenuhi syarat berikut:
- Perangkat Lunak:Python 3.10 atau lebih baru.
- Library Python: paramiko, colorama, prettytable.
- Virtualisasi: VirtualBox / VMware (untuk simulasi server).
- Lingkungan Jaringan (Topologi):Aplikasi membutuhkan 3 Virtual Machine (VM) Linux dengan layanan SSH aktif.
- WEB-SRVMAIL-SRVINT-SRV(Detail konfigurasi IP ada di dalam folder v3_final)📥 

## 👥 Tim Pengembang

Proyek ini dikerjakan oleh **Kelompok 4 (Kelas B1)** - Program Studi Sarjana Terapan Teknologi Rekayasa Internet, Sekolah Vokasi, Universitas Gadjah Mada.

| Nama Lengkap | NIM | Peran | Tanggung Jawab Utama |
| :--- | :--- | :--- | :--- |
| **Muhammad Daffa Izdihar** | 25/560183/SV/26399 | *Project Manager* | Mengatur *timeline* & *workflow*, menyusun dokumentasi laporan, dan supervisi tim. |
| **Ali Sajjad Makarim** | 25/566079/SV/27440 | *Programmer* | Mengeksekusi kode program, membangun arsitektur server, dan implementasi fitur teknis. |
| **M. Arkhan Rosangga Putra** | 25/566316/SV/27063 | *System Designer* | Merancang logika algoritma aplikasi serta menyusun *System Flowchart* dan *Process Flowchart*. |
| **Alesha Khairunisa** | 25/564808/SV/26870 | *System Analyst* | Menganalisis evaluasi program, melakukan pengujian (*testing*), dan validasi output data. |

### **Catatan Penggunaan:**
1.  **Struktur Folder:** Pastikan Anda benar-benar membuat folder `v1_alpha`, `v2_beta`, dan `v3_final` di repository Anda agar link di bagian "Evolusi Versi" berfungsi.
2.  **Gambar Badges:** Kode di bagian atas akan otomatis memunculkan *badges* keren (Python version, Status, License) saat di-render oleh GitHub.
3.  **Nama File:** Simpan konten di atas dengan nama file `README.md` (huruf kapital semua disarankan) di folder paling luar (*root directory*) proyek Anda.
