import socket

HOST = '127.0.0.1'
PORT = 3333  # Must match suspicious port


def run_local_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"[LOCAL SERVER] Listening on {HOST}:{PORT}...")
        while True:
            conn, addr = s.accept()
            print(f"[LOCAL SERVER] Connection from {addr}")
            try:
                conn.sendall(b"Hello, miner?\n")
            except BrokenPipeError:
                print("[LOCAL SERVER] Broken pipe when sending data")
            finally:
                conn.close()


if __name__ == "__main__":
    run_local_server()
