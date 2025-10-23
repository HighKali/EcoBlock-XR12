#!/usr/bin/env python3
import json, os
from datetime import datetime

ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
url = "URL non disponibile"
if os.path.exists("scripts/eco_light_tunnel.json"):
    with open("scripts/eco_light_tunnel.json") as f:
        url = json.load(f).get("url", url)

guest = "Collaboratore non firmato"
if os.path.exists("scripts/eco_light_guests.txt"):
    with open("scripts/eco_light_guests.txt") as f:
        lines = [x.strip() for x in f if x.strip() and not x.startswith("#")]
        if lines: guest = lines[-1]

msg = f"⚡ EcoBlock LIVE\n🪪 {guest}\n🌐 {url}\n⏱️ {ts}"

# Simulazione invio
print(f"📤 Notifica inviata:\n{msg}")
