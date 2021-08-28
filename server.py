import socket
from utils import cpfValidator

HOST = '127.0.0.1'  
PORT = 65432

NAMING_HOST = '127.0.0.1'
NAMING_PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((NAMING_HOST, NAMING_PORT))
    data = 'create-name-service;cpfValidator;'+HOST+';'+str(PORT)
    s.sendall(data.encode())
    s.close()

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