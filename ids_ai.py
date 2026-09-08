import json, subprocess

result = subprocess.run(
    ['cat', '/var/log/suricata/eve.json'],
    capture_output=True, text=True
)

def label_risk(severity):
    if severity == 1:
        return "HIGH"
    elif severity == 2:
        return "MEDIUM"
    return "LOW"

for line in result.stdout.splitlines():
    if '"event_type":"alert"' not in line:
        continue
    try:
        event = json.loads(line)
        alert = event.get("alert", {})
        signature = alert.get("signature", "Unknown")
        severity = alert.get("severity", 3)
        src_ip = event.get("src_ip", "unknown")
        dest_ip = event.get("dest_ip", "unknown")
        print(label_risk(severity) + " | " + signature + " | " + src_ip + " -> " + dest_ip)
    except:
        continue
