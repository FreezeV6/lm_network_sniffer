from ip_lookup import get_ip_info
from process_mapper import map_connection_to_process
from utils import log_alert
from scapy.layers.inet import IP, TCP

SUSPICIOUS_PORTS = {3333, 4444, 5555, 14444, 1688}
SUSPICIOUS_DOMAINS = ["mine", "pool", "hashvault", "nicehash"]


def analyze_packet(pkt):
    if IP in pkt and TCP in pkt:
        dst_ip = pkt[IP].dst
        dst_port = pkt[TCP].dport

        if dst_port in SUSPICIOUS_PORTS:
            reason = f"Connection to suspicious port {dst_port}"
            handle_alert(dst_ip, dst_port, reason)
        else:
            org, desc = get_ip_info(dst_ip)
            if any(domain in desc.lower() for domain in SUSPICIOUS_DOMAINS):
                reason = f"Domain match found: {desc}"
                handle_alert(dst_ip, dst_port, reason)


def handle_alert(ip, port, reason):
    process = map_connection_to_process(ip, port)
    log_alert(ip, port, reason, process)
