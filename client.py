import socket
import time

host = "0.0.0.0"  
port = 11111  
def start_client():
    server_address = ('localhost',11111)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    while True:
           
        command = input("Enter command (check_balance, deposit, withdraw): ")
        account_number = input("Enter account number: ")
        pin = int(input("Enter PIN: "))

        request = f"{command} {account_number} {pin}"
        client_socket.sendall(request.encode("utf-8"))

          
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")

if __name__ == '__main__':
    print("[INFO] Connecting to server...")
    start_client()
