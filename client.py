import socket

HOST = '127.0.0.1'
PORT = 65431

HOST_SERVER = ''
PORT_SERVER = 0


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    name = 'cpfValidator'
    name = name.encode()
    s.sendall(name)
    data = s.recv(1024)
    data = data.decode()
    data = data.split(':')
    HOST_SERVER = data[0]
    PORT_SERVER = int(data[1])

while True:
    print("Digite os numeros do CPF sem pontuacao (0 para sair)")
    cpf = input()
    if cpf == '0':
        quit()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST_SERVER, PORT_SERVER))
        cpf = cpf.encode()
        s.sendall(cpf)
        data = s.recv(1024)
        

    print('Resultado:', repr(data.decode()))
    print('\n')