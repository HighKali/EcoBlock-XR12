#!/usr/bin/env python3
import zipfile, time

ts = time.strftime("%Y%m%d_%H%M%S")
with zipfile.ZipFile(f"eco_light_backup_{ts}.zip", "w") as zipf:
    zipf.write("scripts/eco_light_log.json")
    zipf.write("dashboard/eco_light_panel.html")
    zipf.write("dashboard/assets/eco_light_qr_btc.png")
    zipf.write("dashboard/assets/eco_light_qr_doge.png")
    zipf.write("dashboard/assets/eco_light_tunnel_qr.png")
print(f"🗂️ Backup creato: eco_light_backup_{ts}.zip")

