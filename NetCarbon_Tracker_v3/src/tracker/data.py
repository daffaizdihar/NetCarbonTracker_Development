# === Materi 11 & 12: Functions & Modular Programming ===
# Modul data.py

import paramiko, re


def ambil_data(host, username):
	"""Ambil data CPU & RAM dari server melalui SSH"""
	client = None
	try:
		# Membuat koneksi SSH
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(host, username=username)

		# --- CPU USAGE ---
		_, out, _ = client.exec_command("top -bn1 | grep 'Cpu(s)'")
		m = re.search(r"(\d+\.\d+)\s*id", out.read().decode())
		cpu = round(100 - float(m.group(1))) if m else 0.0

		# --- RAM USAGE ---
		_, out, _ = client.exec_command("free -m")
		total, used = 1, 0
		for line in out.read().decode().splitlines():
			if line.startswith("Mem:"):
				p = line.split()
				if len(p) >= 3:
					total, used = float(p[1]), float(p[2])
				break
		ram = round((used / total) * 100, 2)
		return {"cpu": cpu, "ram": ram}

	except Exception as e:
		print(f"Gagal koneksi ke {ip}: {e}")
		return {"cpu": 0.0, "ram": 0.0}

	finally:
		# Pastikan koneksi SSH ditutup jika sudah dibuat
		if client: client.close()

