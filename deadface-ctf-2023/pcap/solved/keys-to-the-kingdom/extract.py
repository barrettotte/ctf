from scapy.all import rdpcap
from scapy.layers.inet import IP, TCP

pcap_file = './Thekeytothekingdom.pcap'

packets = rdpcap(pcap_file)
streams_combined_data = {}

for packet in packets:
    if TCP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        stream_key = (src_ip, src_port, dst_ip, dst_port)

        if stream_key not in streams_combined_data:
            streams_combined_data[stream_key] = b''
        streams_combined_data[stream_key] += bytes(packet[TCP].payload)

for stream_key, combined_data in streams_combined_data.items():
    print(f"Stream: {stream_key}")
    data = combined_data.decode('utf-8', errors='ignore')
    
with open('payload.jpg', 'wb+') as f:
    f.write(combined_data)
