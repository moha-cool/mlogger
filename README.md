# 🌍 Geo IP Lookup Tool

Ein einfaches CLI-Tool zur IP-Geolokalisierung mit Python.  
Zeigt Land, Stadt, Postleitzahl, Koordinaten und Zeitzone einer IP-Adresse an.

---

## Features

- 🔎 IP → Standortauflösung
- 🌎 Land, Stadt, Postleitzahl
- 📍 Latitude & Longitude
- 🕒 Zeitzone
- 💻 Terminal-Interface mit Banner
- 🎨 Farben im Terminal

---

## Installation

1. Repository klonen:

```bash
git clone https://github.com/moha-cool/mlogger.git
cd mlogger
pip install -r requirements.txt
python main.py

     termux
# 1️⃣ Termux aktualisieren und wichtige Pakete installieren
pkg update -y && pkg upgrade -y
pkg install -y git python clang make wget curl libffi libcrypt libxml2 libxslt tar

# 2️⃣ Pip prüfen und aktualisieren
python -m ensurepip
python -m pip install --upgrade pip

# 3️⃣ Virtuelle Umgebung erstellen und aktivieren
python -m venv venv
source venv/bin/activate

# 4️⃣ mlogger klonen
git clone https://github.com/moha-cool/mlogger.git
cd mlogger

# 5️⃣ Python-Abhängigkeiten installieren
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 6️⃣ GeoLite2-Datenbank herunterladen (optional, falls für mlogger nötig)
mkdir -p ~/GeoLite2 && cd ~/GeoLite2
wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
tar -xzf GeoLite2-City.tar.gz
cd ~/mlogger

# 7️⃣ mlogger starten
python main.py
