import psutil

def map_connection_to_process(target_ip, target_port):
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr and conn.raddr.ip == target_ip and conn.raddr.port == target_port:
            try:
                proc = psutil.Process(conn.pid)
                return f"{proc.name()} (PID: {proc.pid})"
            except:
                return "Unknown process"
    return "No matching process"
