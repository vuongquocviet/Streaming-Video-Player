import socket as sk

from Servers.Entity.Camera import Camera
from Servers.Entity.VideoFile import Video_File
from Servers.Handle.SendData import Send_Data

IP = 'localhost'
PORT = 5555

socket = sk.socket()
socket.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)

socket.bind((IP, PORT))
socket.listen(True)

camera = Camera()
camera.start()

while True:
    connec, addr = socket.accept()
    print  addr
    send = Send_Data(connec, camera)
    send.start()

camera.stop()
socket.close()



