from scapy.all import *
import base64
import binascii

domain = '.pumpkincorp.com.'
packets = rdpcap('capture.pcap')

all_bytes = bytearray()

for packet in packets:
    if packet.haslayer(DNSQR) and packet[IP].dst == '192.168.1.10':
        query = packet[DNSQR].qname
        # print(packet[DNSQR])
       
        # payload = query[0:(len(query)-len(domain))]
        # print(base64.b64decode(query))

        query_bytes = query[:-len(domain)]
        # print(query_bytes.decode())
        # print("".join(map(chr, query_bytes)))
        # all_bytes.append(query_bytes)
        # all_bytes.extend(query_bytes)

        query_hex = binascii.unhexlify(query_bytes)
        # print(query_hex)
        all_bytes.extend(query_hex)


        # query_hex = binascii.hexlify(query_bytes)
        # print(query_hex)
        # print()

print(all_bytes)
#print(binascii.unhexlify(all_bytes))
# print(all_bytes.decode())

with open('payload.docx', 'wb+') as f:
    f.write(all_bytes)
print(all_bytes[0:8])

