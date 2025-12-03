# === Materi 11 & 12: Functions & Modular Programming ===
# === Materi 10: Operasi Matriks (Penjumlahan Total) ===

IDLE_WATT = 50
MAX_WATT = 200
FAKTOR_EMISI = 0.785 # kg CO2 per kWh
#Sumber: Climate Transparency Report 2022 - Indonesia Country Profile
# "For each kilowatt hour of electricity, 784.8 g of CO2 are emitted in Indonesia."
# https://www.climate-transparency.org/wp-content/uploads/2022/CT2022-Indonesia-Web.pdf

# === Materi 11: Functions ===
def estimasi_daya(cpu):
	""" Estimasi daya berdasarkan CPU usage"""
	return round(IDLE_WATT + (cpu/100)*(MAX_WATT - IDLE_WATT), 2)

def hitung_energi(watt, interval=300):
	"""Konversi watt -> kWh berdasarkan waktu (detik)"""
	return round((watt * interval) / 3_000_000, 6)

def kalkulasi_co2(kwh):
	"""Hitung emisi CO2 dari konsumsi energi (kg)"""
	return round(kwh * FAKTOR_EMISI, 6)

