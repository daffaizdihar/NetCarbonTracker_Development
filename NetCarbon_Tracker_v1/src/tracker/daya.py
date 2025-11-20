# === Materi 11 & 12: Functions & Modular Programming ===
# Modul daya.py

# === Materi 2: Variable, Tipe Data, dan Operator ===
IDLE_WATT = 50
MAX_WATT = 200
EMISSION_FACTOR = 0.785 # kg CO2 per kWh
# Sumber: Climate Transparency Report 2022 - Indonesia Country Profile
# "For each kilowatt hour of eletricity, 784.8 g of CO2 are emitted in Indonesia."
# https://www.climate-transparency.org/wp-content/uploads/2022/CT2022-Indonesia-Web.pdf

# === Materi 11: Functions ===
def estimasi_daya(cpu_percent):
    power = IDLE_WATT + (cpu_percent / 100) * (MAX_WATT - IDLE_WATT)
    return round(power, 2)

def hitung_energi(power_watt, interval_seconds):
    kwh = (power_watt * (interval_seconds / 3600)) / 1000
    return round(kwh, 6)

def kalkulasi_co2(kwh):
    co2 = kwh * EMISSION_FACTOR
    return round(co2, 6)
