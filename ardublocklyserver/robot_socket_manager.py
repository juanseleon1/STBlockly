import socket

from ardublocklyserver.STConstants import STport  

class RobotSocketManager:
    def get_connection(self, ip):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        connection.connect((ip, STport))  
        connection.settimeout(60)
        return connection

    def send_msg(self, conex_details, msg, ack= None):
        response = True
        s= self.get_connection(conex_details)
        print("MIRAR2", msg)
        s.send(msg.encode('UTF-8'))
        ret = s.recv(1024)      
        if ack is not None:
            print(ret, ack, int(ret) == int(ack))
            response = int(ret) == int(ack)
        s.close()
        print("MIRAR3", response)
        return response

