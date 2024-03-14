import socket
import json

def exchange(hex_list, value=0):

    # Configure according to your setup
    # host = '127.0.0.1'  # The server's hostname or IP address
    # port = 1337        # The port used by the server
    
    host = '94.237.48.117'
    port = 32131

    cs=0 # /CS on A*BUS3 (range: A*BUS3 to A*BUS7)
    
    usb_device_url = 'ftdi://ftdi:2232h/1'

    # Convert hex list to strings and prepare the command data
    command_data = {
        "tool": "pyftdi",
        "cs_pin":  cs,
        "url":  usb_device_url,
        "data_out": [hex(x) for x in hex_list],  # Convert hex numbers to hex strings
        "readlen": value
    }
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # Serialize data to JSON and send
        s.sendall(json.dumps(command_data).encode('utf-8'))
        
        # Receive and process response
        data = b''
        while True:
            data += s.recv(1024)
            if data.endswith(b']'):
                break
                
        response = json.loads(data.decode('utf-8'))
        # print(f"Received: {response}")
    return response


# Example command
# jedec_id = exchange([0x9F], 3)
# print(jedec_id)
# [239, 64, 24]

# 0x4B = read unique id
# keys = exchange([0x4B], 3)
# print(keys)
# [210, 102, 180]

# Security Register Address:
# Security Register 1: A23-16 = 00h; A15-8 = 10h; A7-0 = byte address
# Security Register 2: A23-16 = 00h; A15-8 = 20h; A7-0 = byte address
# Security Register 3: A23-16 = 00h; A15-8 = 30h; A7-0 = byte address

# 0x48 = read security register
reg_1 = exchange([0x48, 0x00, 0x10, 0x10], 64)
print('security register 1:', reg_1)

reg_2 = exchange([0x48, 0x00, 0x20, 0x10], 64)
print('security register 2:', reg_2)

reg_3 = exchange([0x48, 0x00, 0x30, 0x10], 64)
print('security register 3:', reg_3)

# Read Data 03h A23-A16 A15-A8 A7-A0 (D7-D0)
d = exchange([0x03, 0x0, 0x0, 0x0, 0x0], 64)
print('d:', d)

print(''.join([chr(c) for c in d]))
# HTB{m3m02135_57023_53c2375_f02_3v32y0n3_70_533!@}
