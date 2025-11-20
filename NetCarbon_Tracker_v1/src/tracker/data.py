# === Materi 11 & 12: Functions & Modular Programming ===
# Modul data.py

import paramiko

# === Materi 2: Variabel, Data Types, Operators ===
# Fungsi untuk mengambil data CPU dan RAM dari server
def metrik(host, username):
    # === Materi 3: Input-Output ===
    print(f"\nMengambil data dari {host} ...")

    # Membuat Koneksi SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username)

    # Menjalankan perintah untuk CPU dan RAM
    stdin, stdout, stderr = ssh.exec_command("top -bn1 | grep 'Cpu(s)'")
    cpu_line = stdout.read().decode()
    stdin, stdout, stderr = ssh.exec_command("free -m | grep Mem")
    mem_line = stdout.read().decode()
    ssh.close()

    # == Materi 4: Conditional Statemetns ===
    if "id" in cpu_line:
        # Parsing CPU idle untuk mendapatkan persentase penggunaan
        idle = float(cpu_line.split("id")[0].split(",")[-1].strip())
        cpu_used = round(100 - idle, 2)
    else:
        cpu_used = 0.0

    # Parsing RAM dari perintah free -m
    parts = mem_line.split()
    total = float(parts[1])
    available = float(parts[6])
    ram_used = round(((total - available) / total ) * 100, 2)

    # === Materi 7: Dictionary ===
    data = {
        "cpu": cpu_used,
        "ram": ram_used
    }

    return data