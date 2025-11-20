# NetCarbon Tracker v3.0
Versi paling lengkap dan matang dari NetCarbon Tracker: realtime monitoring, 3-level emission status, dan database logging per menit.

---

## 📌 Deskripsi Singkat
NetCarbon Tracker v3.0 membawa kemampuan enterprise-grade, termasuk:
- simulasi 19.200 server,
- status emisi warna biru–hijau–merah,
- dan penyimpanan rata-rata emisi karbon per menit ke dalam database SQLite.

Versi ini dirancang untuk pemantauan datacenter skala besar dengan visualisasi yang tetap ringan dan cepat.

---

## ✨ Fitur Baru vs v2.0
### 🔵🟢🔴 Tiga Level Status Emisi
- **Biru**: < 0.70 → Emisi rendah (eco-friendly)  
- **Hijau**: 0.70 – 0.85 → Normal & stabil  
- **Merah**: > 0.85 → Warning melebihi batas  

### 🗄 Sistem Database (SQLite)
- Mencatat average CO₂ setiap 1 menit  
- Data dapat diekspor atau dianalisis ulang  
- Tampil langsung di layar (recent 5 averages)

### 🌐 Simulasi Datacenter Enterprise
- 3 server × 6400 simulasi = **19.200 server total**

### 🎛 Output tetap realtime dan ringan
Tidak merubah cara kerja utama, hanya menambah fitur tambahan.

---

## 📐 Algoritma Utama v3.0
1. Mulai program  
2. Inisialisasi variabel & buffer menit  
3. Tampilkan judul  
4. Loop pemantauan realtime  
5. Ambil data dari server  
6. Hitung daya → energi → emisi  
7. Kalikan faktor simulasi  
8. Tambahkan total CO₂ ke buffer  
9. Jika 60 detik terlewati:  
   - Hitung rata-rata CO₂ per menit  
   - Simpan ke database  
   - Tampilkan average CO₂ terbaru  
10. Tampilkan tabel monitoring  
11. Tampilkan status emisi 3 level  
12. Delay beberapa detik  
13. Ulangi  
14. CTRL+C → selesai  

---

## 🚀 Improvement vs v2.0
- Database logging (historical analysis)
- Emission classification lebih detail (3 level)
- Sistem buffer per menit
- Output lebih informatif
- Simulasi skala enterprise

---

## 📊 Status Dashboard (contoh)
- CPU, RAM, Power, kWh per server  
- Total emisi seluruh server × simulasi  
- Warna status: Biru/Hijau/Merah  
- Average emisi per menit dari database  

---

## 🎯 Status
Versi 3.0 merupakan versi paling stabil dan dapat dipublikasikan sebagai portofolio profesional dalam bidang:
- Cloud & SysAdmin  
- Networking  
- Python programming  
- DevOps  
- Sustainability Technology (Green IT)  
