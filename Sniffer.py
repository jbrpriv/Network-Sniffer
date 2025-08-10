import socket
from scapy.all import Ether

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Starting packet capture... Press Ctrl+C to stop.")

try:
    while True:
        raw_data, addr = s.recvfrom(65535)
        packet = Ether(raw_data)
        print(packet.summary())
except KeyboardInterrupt:
    print("\nStopping packet capture.")
    s.close()
