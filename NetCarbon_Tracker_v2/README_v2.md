 # NetCarbon Tracker v2.0
Versi yang membawa perubahan besar: monitoring realtime, status emisi, dan simulasi skala ribuan server.

---

## 📌 Deskripsi Singkat
NetCarbon Tracker v2.0 memperkenalkan mode monitoring realtime (live updating) serta penetapan status emisi "Normal" dan "Warning". Program ini juga mulai mensimulasikan skala server besar (hingga 16.000 ekivalen server).

Selain itu, faktor emisi diperbarui menjadi 0.78 kg CO₂/kWh berdasarkan acuan ilmiah dari Climate Transparency Report 2022.

---

## ✨ Fitur Baru vs v1.0
- **Realtime monitoring (while True loop)**
- **Refresh layar otomatis**
- **Penanda status emisi**  
  - Hijau: Emisi di bawah batas  
  - Merah: Emisi melebihi batas  
- **Simulasi skala besar: 3 server × 5333 = 16.000 server**
- **Faktor emisi updated: 0.78 (lebih ilmiah)**
- Output tabel realtime setiap beberapa detik

---

## 📐 Algoritma Utama v2.0
1. Mulai program  
2. Inisialisasi variabel  
3. Tampilkan judul  
4. Masuk ke loop pemantauan (infinite loop)  
5. Inisialisasi list hasil  
6. Loop server  
7. SSH → ambil CPU & RAM  
8. Hitung daya dan CO₂  
9. Simpan hasil ke list  
10. Hitung total energi dan CO₂  
11. Bersihkan layar  
12. Tampilkan tabel hasil  
13. Tampilkan status emisi  
14. Delay beberapa detik  
15. Ulangi  
16. CTRL + C → Selesai  

---

## 🚀 Improvement vs v1.0
- Enhanced realtime experience  
- Emission awareness system  
- Stronger scientific basis  
- Simulasi skala besar untuk studi kasus industri  

---

## 🚫 Limitasi v2.0
- Belum ada penyimpanan database  
- Belum memiliki kategori emisi bertingkat  
- Tidak menyimpan histori emisi  

---

## 🎯 Status
Versi 2.0 menjadi fondasi versi 3.0: realtime + database + kategori emisi 3 warna.
