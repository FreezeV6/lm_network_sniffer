from scapy.all import IP, TCP, send

def send_test_packet():
    packet = IP(dst="127.0.0.1")/TCP(dport=3333)
    send(packet, iface="Npcap Loopback Adapter", verbose=0)
    print("[TEST] Test packet sent to 127.0.0.1:3333")

if __name__ == "__main__":
    send_test_packet()