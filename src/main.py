from analyzer import analyze_packet
from scapy.all import sniff


def start_sniffer():
    print("[INFO] Sniffer started. Press Ctrl+C to stop.")
    sniff(filter="ip", prn=analyze_packet, store=0)


if __name__ == "__main__":
    start_sniffer()