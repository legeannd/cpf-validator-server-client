import socket

HOST = '127.0.0.1'
PORT = 65432

while True:
    print("Digite os numeros do CPF sem pontuacao (0 para sair)")
    cpf = input()
    if cpf == '0':
        quit()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        cpf = cpf.encode()
        s.sendall(cpf)
        data = s.recv(1024)
        

    print('Resultado:', repr(data.decode()))
    print('\n')