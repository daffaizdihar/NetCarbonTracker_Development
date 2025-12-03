# === Materi 11 & 12: Pemrograman Modular & Functions ===
# Modul tampilan.py

# === Materi 11: Functions ===
def tampilkan_judul():
	"""Tampilkan judul rpgram di layar"""
	print("\n=== NetCarbon Tracker v3.0 (Realtime Live Update Mode) ===\n")


def tampilkan_tabel(results, total_energi, total_co2):
	"""Tampilkan tabel hasil monitoring"""
	print("\n" + "=" * 60)
	print(" " * 5 + "NetCarbon Tracker v3.0 (Realtime Live Update Mode)")
	print("="*60)
	print(f"{'Server Name':<12}{'CPU(%)':<8}{'RAM(%)':<8}{'Power(W)':<10}{'kwh':<10}{'CO2(kg)':<10}")
	print("-"*60)
	for row in results:
		print(f"{row[0]:<12}{row[1]:<8.1f}{row[2]:<8.1f}{row[3]:<10.1f}{row[4]:<10.6f}{row[5]:<10.6f}")
	print("-"*60)
	print(f"{'TOTAL':<12}{'-':<8}{'-':<8}{'-':<10}{total_energi:<10.3f}{total_co2:<10.3f}")
	print("="*60)

def tampilkan_status(total_co2, batas):
	"""Tampilkan status emisi dengan 3 level warna"""

	if total_co2 < 0.70:
		# Warna BIRU (aman sekali)
		print("\033[1;34m" + "-" * 60 + "\033[0m")
		print("\033[1;34m" + "EMISI RENDAH - Sangat Ramah Lingkungan".center(60) + "\033[0m")
		print("\033[1;34m" + "-" * 60 + "\033[0m")

	elif 0.70 <= total_co2 <= 0.85:
		# Warna HIJAU (normal)
		print("\033[1;32m" + "-" * 60 + "\033[0m")
		print("\033[1;32m" +"Emis Normal - Intensitas Emisi Stabil".center(60) + "\033[0m")
		print("\033[1;32m" + "-" * 60 + "\033[0m")

	else:
		# Warna MERAH (warning)
		print("\033[1;31m" + "-" * 60 + "\033[0m")
		print("\033[1;31m" + "WARNING - Emisi Melebihi Batas!".center(60) + "\033[0m")
		print("\033[1;31m" + "-" * 60 + "\033[0m")

def tampilkan_pesan_stop():
	"""Pesan saat monitoring dihentikan"""
	print("\n Monitoring dihentikan oleh pengguna.\n")
