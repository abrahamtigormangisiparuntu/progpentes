import socket
import sys
from getopt import getopt

print("ini adalah CLIENT ")

# Bikin socketnya, deklasi s sebagai socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host yang digunakan client
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "IP:", ip)

# identitas client dan tujuan
host = "127.0.0.1"
port = 2000
name = "ClientSide" 
client.connect((host, port))
print("Terhubung...")

# kirim nama ke TCP
client.send(name.encode())

# terima pesan dari TCP
fromServer = client.recv(1024)
fromServer = fromServer.decode()
print(fromServer, "berhasil terhubung")
print("Tekan (exit) untuk meninggalkan ruangan...\n")

while True:
    # terima pesan dari TCP
    message = client.recv(1024)
    message = message.decode()
    # kirim pesan ke TCP
    print(fromServer, ":", message)
    message = input(name + ":")
    if message == 'exit':
        message = "Meninggalkan ruangan..."
        client.send(message.encode())
        print(" ")
        break
    client.send(message.encode())



    
    
