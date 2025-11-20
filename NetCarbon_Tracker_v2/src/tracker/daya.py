# === Materi 11 & 12: Functions & Modular Programming ===
# === Materi 10: Operasi Matriks (Penjumlahan Total) ===

FAKTOR_EMISI = 0.82
IDLE_WATT, MAX_WATT = 50, 200 # Daya minimum dan maksimum server

def estimasi_daya(cpu):
	"""" Estimasi daya berdasarkan CPU usage"""
	return round(IDLE_WATT + (cpu/100)*(MAX_WATT - IDLE_WATT), 2)

def hitung_energi(watt, interval=300):
	"""Konversi watt -> kWh berdasarkan waktu (detik)"""
	return round((watt * interval) / 3_000_000, 6)

def kalkulasi_co2(kwh):
	"""Hitung emisi CO2 dari konsumsi energi (kg)"""
	return round(kwh * FAKTOR_EMISI, 6)

