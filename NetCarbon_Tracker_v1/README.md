# NetCarbon Tracker v1.0
Sistem monitoring server sederhana berbasis Python untuk memantau kinerja CPU dan estimasi emisi karbon. Versi pertama ini merupakan fondasi dari seluruh pengembangan NetCarbon Tracker.

---

## 📌 Deskripsi Singkat
NetCarbon Tracker v1.0 mengambil data CPU dan RAM dari tiga server Linux menggunakan SSH, kemudian menghitung estimasi daya, energi, dan emisi karbon berdasarkan faktor emisi awal (0.82 kg CO₂/kWh).

Versi ini masih bersifat sederhana dan tidak menampilkan data secara live.

---

## ✨ Fitur Utama
- Monitoring CPU & RAM via SSH menggunakan Paramiko.
- Perhitungan energi dan CO₂ berdasarkan:
  - Estimasi daya dari CPU usage.
  - Konversi Watt → kWh.
  - Faktor emisi 0.82.
- Output berupa tabel sederhana (1 kali tampil).
- Topologi menggunakan 3 server:
  - WEB-SRV  
  - MAIL-SRV  
  - INT-SRV  

---

## 📐 Algoritma Utama v1.0
1. Mulai program  
2. Inisialisasi daftar server  
3. Loop 3 server:  
   - SSH → ambil data CPU & RAM  
   - Hitung daya, energi, CO₂  
4. Tampilkan tabel hasil  
5. Program selesai  

---

## 🚫 Limitasi v1.0
- Tidak realtime / tidak live update  
- Tidak ada peringatan emisi  
- Simulasi server terbatas (3 server)
- Faktor emisi belum berdasarkan data referensial ilmiah  
- Tidak ada sistem database  

---

## 🎯 Status
Versi 1.0 menjadi dasar untuk pengembangan fitur realtime dan analisis emisi pada versi berikutnya.
