# check_io_connections.py
import psutil
import subprocess


def check_io():
    # Example check for disk I/O
    disk_io = psutil.disk_io_counters()
    print(f"Read Count: {disk_io.read_count}, Write Count: {disk_io.write_count}")


def get_network_connections():
    try:
        result = subprocess.run(['sysctl', '-a', 'net.inet.tcp'], capture_output=True, text=True)
        output = result.stdout

        connections = []
        for line in output.splitlines():
            if 'net.inet.tcp.pcblist' in line:
                connections.append(line)
        
        return connections

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    check_io()
    connections = get_network_connections()
    for conn in connections:
        print(conn)


