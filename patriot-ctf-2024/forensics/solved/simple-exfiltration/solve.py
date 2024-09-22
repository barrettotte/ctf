from scapy.all import rdpcap, IP, ICMP

target_ip = '192.168.237.132'
packets = rdpcap('exfiltration_activity_pctf_challenge.pcapng')

ttl = []
for packet in packets:
    if (ICMP in packet and IP in packet) and (packet[IP].src == target_ip) and (packet[IP].ttl <= 126):
        ttl.append(chr(packet[IP].ttl))

print(''.join(ttl))
# pctf{time_to_live_exfiltration}
