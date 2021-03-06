import socket
from utils import cutter

HOST = '127.0.0.1'  
PORT = 65431

names_dict = {}

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:            
            while True:
                data = conn.recv(1024)
                data = data.decode()
                
                if not data:                    
                    break
                if('create-name-service' in data):                
                    data = cutter(data)

                    identificador = data[0]
                    endereco = data[1]
                    porta = data[2]
                    
                    names_dict[identificador] = endereco+':'+porta
                    print(names_dict)
                else:
                    ip = str(names_dict[data])
                    ip = ip.encode()

                    if(not ip):
                        conn.sendall(b'Servico nao encontrado')
                    else:
                        conn.sendall(ip)