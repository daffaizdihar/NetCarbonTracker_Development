# === tracker/tampilan.py ===
# Materi 11: Functions | Materi 12: Modular Programming ===

def tampilkan_judul():
	"""Tampilkan judul program di layar"""
	print("\n=== NetCarbon Tracker v2.0 (Realtime Live Update Mode) ===\n")

def tampilkan_tabel(results, total_kwh, total_co2):
	"""Menampilkan tabel hasil monitoring"""
	print("\n" + "=" * 60)
	print(" " * 5 + "NetCarbon Tracker v2.0 (Realtime Live Update Mode)")
	print("="*60)
	print(f"{'Server Name':<12}{'CPU(%)':<8}{'RAM(%)':<8}{'Power(W)':<10}{'kwh':<10}{'CO2(kg)':<10}")
	print("-"*60)
	for row in results:
		print(f"{row[0]:<12}{row[1]:<8.1f}{row[2]:<8.1f}{row[3]:<10.1f}{row[4]:<10.6f}{row[5]:<10.6f}")
	print("-"*60)
	print(f"{'TOTAL':<12}{'-':<8}{'-':<8}{'-':<10}{total_kwh:<10.3f}{total_co2:<10.3f}")
	print("="*60)

def tampilkan_status(total_co2, batas):
	"""Tampilkan status emisi dengan warna"""
	if total_co2 > batas:
		print("\033[1;31m" + "-" * 60 + "\033[0m")
		print("\033[1;31m" + "WARNING: Emisi melebihi ambang batas!".center(60) + "\033[0m")
		print("\033[1;31m" + "-" * 60 + "\033[0m")
	else:
		print("\033[1;32m" + "-" * 60 + "\033[0m")
		print("\033[1;32m" + "Emisi Normal - Aman & Efisien".center(60) + "\033[0m")
		print("\033[1;32m" + "-" * 60 + "\033[0m")

def tampilkan_pesan_stop():
	"""Pesan saat monitoring dihentikan"""
	print("\n Monitoring dihentikan oleh pengguna.\n")
