# === NetCarbon Tracker v2.0 (Realtime No-Delay Mode) ===
# === Materi 12: Modular Programming ===
# === Materi 11: Functions ===
# === Materi 5: Loops (while + for) ===

import os, time
from tracker.data import ambil_data
from tracker.daya import estimasi_daya, hitung_energi, kalkulasi_co2
from tracker.tampilan import (
	tampilkan_tabel,
	tampilkan_judul,
	tampilkan_status,
	tampilkan_pesan_stop,
)

# === Materi 1: Algoritma & Flowcharrt ===
servers = [
	{"name": "WEB-SRV", "ip":  "10.10.10.2"},
	{"name": "MAIL-SRV", "ip": "10.10.10.3"},
	{"name": "INT-SRV", "ip": "172.16.10.5"}
]

USERNAME = "monitor"
FAKTOR_SIMULASI = 5333	# Jumlah Server disimulasikan
BATAS_EMISI = 0.82

# === Materi 1: Algoritma
tampilkan_judul()

# === Materi 5: Loops  (For Loop) ===
try:
	while True:
		# Bersihkan layar (simulasi "refresh")
		print("\033[H\033[J", end="") # Reset cursor ke awal

		results = []
		total_kwh = 0
		total_co2 = 0

		for srv in servers:
			data = ambil_data(srv["ip"], USERNAME)
			power = estimasi_daya(data["cpu"])
			kwh = hitung_energi(power, 1)
			co2 = kalkulasi_co2(kwh)

			# === Materi 9: Multi-dimensional Array (Nested list) ===
			results.append([srv["name"], data["cpu"], data["ram"], power, kwh, co2])

			# === Materi 10: Operasi Matriks (Penjumlahan total) ===
			total_kwh += kwh
			total_co2 += co2

		total_kwh *= FAKTOR_SIMULASI
		total_co2 *= FAKTOR_SIMULASI

		# Tampilkan hasil setiap iterasi (Langsung overwrite)
		tampilkan_tabel(results, total_kwh, total_co2)
		print("\n")
		tampilkan_status(total_co2, BATAS_EMISI)
		print(f"\nAmbang batas emisi: {BATAS_EMISI:.3f} kg CO2")
		print(f"Simulasi jumlah server sebenarnya: {FAKTOR_SIMULASI} unit")
		print("\n")
		print("\nTekan CTRL + C untuk menghentikan monitoring...")

		# Delay 1 detik supaya tidak terlalu cepat berubah
		time.sleep(2)

except KeyboardInterrupt:
	tampilkan_pesan_stop()
