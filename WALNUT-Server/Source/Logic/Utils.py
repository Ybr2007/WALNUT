import socket

def SendMsg(connection: socket.socket, msg:str) -> bool:
    try:
        connection.send(msg.encode('utf-8'))
        return True
    except:
        return False

def GetMsg(connection: socket.socket) -> str:
    try:
        return connection.recv(1024).decode('utf-8')
    except:
        return None
