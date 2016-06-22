import socket
import os
import random
SERVER_PORT = 9092
SERVER_IP = "127.0.0.1"
SERVER_BUFFER = 8192

def getCPUtemperature():
    res=os.popen('vcgencmd measure_temp').readline()
    return (res.replace("temp=","").replace("'C\n",""))
    #return random.randint(0,100)
print getCPUtemperature()
try:
    while 1:
        v = raw_input()
        sendopsocket = socket.create_connection((SERVER_IP,SERVER_PORT))
        if v == "g":
            sendopsocket.send("t={}".format(getCPUtemperature()))
            response = sendopsocket.recv(SERVER_BUFFER)
            print response
        if v[0:2] == "gt":
            sendopsocket.send(v)
            response = sendopsocket.recv(SERVER_BUFFER)
            print response
        sendopsocket.close()
except KeyboardInterrupt:
    sendopsocket.close()
