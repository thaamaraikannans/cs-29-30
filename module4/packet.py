from scapy.all import IP, TCP, sniff



# value = IP(dst = "13.203.160.105")/TCP()
# print(value.show())

def save_packet(packet):
    with open("raw.txt", "a") as f:  # Open the file in append mode
        f.write(packet.summary() + "\n")  # Write packet summary
        f.write(str(packet.show(dump=True)) + "\n\n")  # Write detailed packet info

# Sniff to 10 sec for packets and process each one using save_packet
sniff(timeout=10, prn=save_packet)
