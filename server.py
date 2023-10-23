
import socket
import sys
from getopt import getopt

print("ini adalah SERVER")

# bikin socketnya, deklarasi s sebagai socket
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Tentukan IP yang akan digunakan
ip = "127.0.0.1"

# tentukan port yang akan digunakan
port = 2000

# binding host dan port dengan socketnya
server.bind((ip, port))

print("Ip:", ip)
print("port:", port)
name= "abraham"

           
# mulai pendengar TCPnya
server.listen(1)
print("Menunggu koneksi...")

print ("Mohon bersabar jika koneksi lama, mungkin lokasi jauh atau salah mungkin sedang menghafal code untuk kuis lab")

# menerima koneksi client TCP
conection, addr = server.accept()

# untuk menerima respon
fromClient = conection.recv(1024)
fromClient = fromClient.decode()
print(fromClient, "berhasil terhubung")
print("Tekan (exit) untuk meninggalkan ruangan...")


            
conection.send(name.encode())

while True:
    # kirim pesan ke TCP
    message = input(name + ":")
    if message == 'exit':
        message = "Meninggalkan ruangan..."
        conection.send(message.encode())
        break
    # terima message dari TCP
    conection.send(message.encode())
    message = conection.recv(1024)
    message = message.decode()
    print(fromClient, ":", message)

def main():
    global ip , port
    
    opts, _ = getopt(sys.argv[1:], "i:p:s",["ip=","port=", "server"] )
    print(opts)
    
    for opt, value in opts:
        print(f"{opt}:{value}")
        if opt == "-i" or opt == "--ip":
            ip=value
        elif opt == "-p" or opt =="--port":
            port = int(value)

    if ip == "":
        print("Ip must be filled !")
        exit()
    if port >2500 :
        print("Port must be between 2000 and 2500!")
        exit()
    if port <2000 :
        print("Port must be between 2000 and 2500!")
        exit()
    
main()
