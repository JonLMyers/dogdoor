import scapy

def main():
    packet = send(IP(src='127.0.0.1', dst='192.168.1.151')/TCP(sport=443,dport=1337,reserved=1))
    packet = Ether()/IP(src='127.0.0.1', dst='192.168.1.151')/TCP(dport=443,flags='S',reserved=1)     