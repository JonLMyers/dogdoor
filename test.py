import socket
import struct
import pyshark
import win32serviceutil
import servicemanager
import win32event
import win32service

def main():
    capture = pyshark.LiveCapture(bpf_filter='(tcp src port 1337)')
    while True:
        for packet in capture.sniff_continuously(packet_count=50):
            print('Just arrived:', packet)


main()