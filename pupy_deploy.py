import scapy

def main():
    packet = Ether()/IP(src='127.0.0.1', dst='192.168.1.151')/TCP(dport=443,flags='S',reserved=1)     