import socket
import struct
import binascii
import pyshark
import win32serviceutil
import servicemanager
import win32event
import win32service

def deploy_config(hex_data):
    # pyshark LayerObject to string
    hex_data = str(hex_data)
    # string to Formatted string
    hex_str = hex_data.replace(':', '')
    #Formatted string to formated hex(0x00 -> 00)
    raw_hex = hex(int(hex_str, 16))[2:]
    #fromated hex to decoded string
    print(bytearray.fromhex(raw_hex).decode())

def test_deploy_config():
    deploy_config("68:75:6c:6c:6f")

def main():
    # Offset (4) Reserved (3) NS flag (1)
    # 0000 0010
    capture = pyshark.LiveCapture(bpf_filter='(tcp src port 443) and (tcp[12] & 2 != 0)')
    #capture = pyshark.LiveCapture(bpf_filter='(tcp src port 443) and (tcp dst port 1337)')
    while True:
        for packet in capture.sniff_continuously(packet_count=1):
            deploy_config(packet.tcp.get_field_value("payload"))
            try:
                deploy_config(raw_data)
            except:
                print("Error: No Data")

#main()
test_deploy_config()