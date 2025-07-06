import socket

def send_real_tcp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 3333))
    except Exception as e:
        print(f"[TEST] Connection failed (expected): {e}")
    finally:
        s.close()

if __name__ == "__main__":
    send_real_tcp()
