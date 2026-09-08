# ids-project
# AI-Assisted Intrusion Detection System (IDS)

## Overview
A network-based Intrusion Detection System built on Ubuntu Server
running in VMware. Uses Suricata as the detection engine and a 
custom Python script as the AI triage layer to classify threats
in real time.

## How It Works
1. Suricata monitors all network traffic on the virtual machine
2. When traffic matches a rule, Suricata writes an alert to eve.json
3. The Python script reads eve.json and classifies each alert as
   LOW, MEDIUM, or HIGH risk
4. Results are printed in a readable format for security analysis

## Tech Stack
- VMware Workstation - Hypervisor
- Ubuntu Server - Operating System  
- Suricata 8.0.6 - Network IDS Engine
- Python 3 - AI Triage Layer
- Suricata Community Rules - 50,000+ threat signatures

## What It Detects
- Spotify P2P broadcast traffic
- HTTP attack response patterns
- GNU/Linux package manager traffic
- Custom rules for port scans
- SSH brute force attempts
- ICMP ping floods
- Suspicious outbound connections

## Project Structure
ids_ai.py - Main Python script that reads and classifies alerts
README.md - Project documentation

## How To Run
Step 1 - Make sure Suricata is running
sudo systemctl start suricata

Step 2 - Generate test traffic
curl http://testmynids.org/uid/index.html

Step 3 - Run the AI triage script
sudo python3 ids_ai.py

## Example Output
LOW | ET INFO Spotify P2P Client | 172.21.134.139 -> 172.21.135.255
MEDIUM | GPL ATTACK_RESPONSE id check returned root | 18.x.x.x -> 192.168.x.x
HIGH | ET MALWARE Suspicious User-Agent | 10.0.0.5 -> 45.33.32.156

## Risk Classification
HIGH   - Severity 1 - Immediate investigation required
MEDIUM - Severity 2 - Suspicious activity, monitor closely  
LOW    - Severity 3 - Informational, low priority

## AI Layer Explanation
The triage layer uses rule-based severity classification as a 
baseline. The system is designed to be extended with real ML
models or LLM APIs (such as Claude) for natural language alert
summarisation. The current version demonstrates the data pipeline
that an AI model would sit on top of.

## Real World Detections
During testing this IDS detected live Spotify P2P broadcast traffic
across multiple subnets on the network, demonstrating that Suricata
is successfully monitoring real network activity beyond just the VM.

## Future Improvements
- Web dashboard showing live alerts in a browser
- CSV export for reporting and analysis
- Claude AI API integration for plain English alert summaries
- Email alerts for HIGH severity detections
- Live real time monitoring instead of log file reading

## Author: Sahil Kumar
Built as a cybersecurity project demonstrating network intrusion
detection with AI-assisted threat classification.
