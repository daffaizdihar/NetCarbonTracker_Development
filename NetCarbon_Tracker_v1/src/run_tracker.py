# === Materi 1: Algoritma ===
# ALur utama program NetCarbon Tracker

from tracker.data import metrik
from tracker.daya import estimasi_daya, hitung_energi, kalkulasi_co2
from tracker.tampilan import table

# === Materi 8: 1-D Array & List ===
servers = [
    {"name": "WEB-SRV", "ip": "10.10.10.2"},
    {"name": "MAIL-SRV", "ip": "10.10.10.3"},
    {"name": "INT-SRV", "ip": "172.16.10.5"}
]

USERNAME = "monitor"
INTERVAL = 300 # 5 menit

# === Materi 6: Tipe Data Set ===
server_ips = {srv["ip"] for srv in servers} # === Materi 8: 1D Array untuk menyimpan hasil

results = [] # === Materi 8: 1D Array untuk menyimpan hasil ===

for srv in servers:
        metrics = metrik(srv["ip"], USERNAME)
        # === Materi 9: Multi-dimensional Array ===
        # Data per server dimasukkan sebagai list dalam list
        power = estimasi_daya(metrics["cpu"])
        kwh = hitung_energi(power, INTERVAL)
        co2 = kalkulasi_co2(kwh)

        results.append([srv["name"], metrics["cpu"], metrics["ram"], power, kwh, co2])

# === Materi 10: Operasi Matriks (Penjumlahan total nilai) ===
total_energi = sum([r[4] for r in results ])
total_co2 = sum([r[5] for r in results])

# === Materi 3: Input/Output Function Implementation ===
from tracker.tampilan import table
table (results, total_energi, total_co2)

