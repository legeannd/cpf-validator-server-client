import socket
from utils import cpfValidator

HOST = '127.0.0.1'  
PORT = 65432

while True:    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:            
        s.bind((HOST, PORT))        
        s.listen()                

        conn, addr = s.accept()
        with conn:                               
            while True:
                data = conn.recv(1024)                
                if not data:                    
                    break
                else:
                    data = data.decode()
                    if(cpfValidator(data)):
                        anwser = 'Este CPF eh valido'                        
                        conn.sendall(anwser.encode())
                    else:
                        anwser = 'Este CPF eh invalido'                        
                        conn.sendall(anwser.encode())