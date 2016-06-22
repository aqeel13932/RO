import socket
from multiprocessing import Process
from threading import Condition
#Server Information
SERVER_PORT = 9092
SERVER_IP = "127.0.0.1"
SERVER_BUFFER= 8192
#Max Clients Server Can Serve
MAX_CLIENTS = 500

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind((SERVER_IP,SERVER_PORT))
clients={}
def HandleClient(socket,addr):

    message = socket.recv(SERVER_BUFFER)
    command=message[0:2]
    print command
    if (command=="t="):
        print addr[0]
        clients[addr[0]]=int(message[3:])
        socket.send(str("OK"))
    elif(command=="gt"):
        print addr[0]
        if message[3:] in clients.keys():
            socket.send(str(clients[message[3:]]))
        else:
            socket.send("Client has not yet reported its CPU temperature")
            
    else:
        socket.send("Unknown")
    print message
    #socket.close()
try:
    while True:
        serversocket.listen(MAX_CLIENTS)
        clientsocket,addr = serversocket.accept()
        HandleClient(clientsocket,addr)
except KeyboardInterrupt:
    serversocket.close()
    clientsocket.close()

    
'''
t=cpu_temp_of_client - This stores the CPU temperature of the client in the server
gt ip_address_of_device - Return the temperature of the device whose ip is ip_address_of_device
If server receives the first command it stores the temp and responds ok. If server receives the second command, it checks if requested device has reported its temperature and responds with the temperature or with Client has not yet reported its CPU temperature. For everything else it responds Unknown command.
You need to write the code for server or client, not both.
'''