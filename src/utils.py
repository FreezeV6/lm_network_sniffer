from datetime import datetime

LOG_FILE = "alerts.log"

def log_alert(ip, port, reason, process):
    msg = f"[{datetime.now()}] ALERT: {ip}:{port} - {reason} - Process: {process}"
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")