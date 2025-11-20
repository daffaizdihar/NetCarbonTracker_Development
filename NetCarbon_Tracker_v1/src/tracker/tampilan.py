# === Materi 11 & 12: Pemrograman Modular & Functions ===
# Modul tampilan.py

# === Materi 11: Functions ===
def table(results, total_energi, total_co2):
    print("="*65)
    print(f"{'Netcarbon Tracker v2.0':^60}")
    print("="*65)
    print(f"{'Server Name':<12}{'CPU(%)':>8}{'RAM(%)':>11}{'Power(W)':>12}{'kwh':>8}{'CO2(kg)':>20}")
    print("-"*65)

    # === Materi 5: Loops ===
    for row in results:
        print(f"{row[0]:<12}{row[1]:>8.2f}{row[2]:>10.2f}{row[3]:>10.1f}{row[4]:>12.6f}{row[5]:>12.6f}")

    print("-"*65)

    # == Materi 10: Operasi Matriks (Penjumlahan total nilai) ===
    print(f"{'TOTAL':<12}{'-':>8}{'-':>10}{'-':>10}{total_energi:>12.3f}{total_co2:>12.3f}")
    print("="*65)