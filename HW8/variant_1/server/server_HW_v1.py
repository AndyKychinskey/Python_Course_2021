"""
Сервер
1. принимает число от Клиента
2. проверяет, действительно ли это простое число
3. записывает число в файл
"""
import socket
import communication
import time
from sympy.ntheory import isprime

err_counter = 0

if __name__ == '__main__':
    _socket = socket.socket()
    _socket.bind((socket.gethostname(), 56 + 13))
    _socket.listen(1)
    print("Starting server...")

    while True:
        clientsocket, address = _socket.accept()
        print(f"Connection from {address} has been established.")
        while True:
            time1 = time.time()
            prime_nums = communication.readMsg(clientsocket)
            print(f'time point 1 is: {time.time() - time1}')
            print(len(prime_nums))
            # validating data
            for index, num in enumerate(prime_nums):
                if( not isprime(num) ):
                    err_counter += 1
                    prime_nums[index] = None
            print(f'time point 2 is: {time.time() - time1}')
            # filtering data
            if(err_counter):
                prime_nums = list(filter(None, prime_nums))
            print(f'err_counter is: {err_counter}')
            clientsocket.close()
            print('Connection closed...')
            # write file: start
            with open("prime_nums.txt", "w") as f:
                f.write(str(prime_nums))
            # write file: end
            # 2.388136625289917
            print(f'time point 3 is: {time.time() - time1}')
            break
