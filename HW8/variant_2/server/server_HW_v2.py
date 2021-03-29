"""
Сервер
1. принимает число от Клиента
2. проверяет, действительно ли это простое число
3. записывает число в файл
"""
import os
import socket
import communication
import time
from sympy.ntheory import isprime
from multiprocessing import Process, Queue, Event, Lock
import concurrent.futures as cf

# if os.path.exists("prime_nums.txt"):
#     os.remove("prime_nums.txt")
#     print("deleted...")

queue, event, lock = Queue(), Event(), Lock()
err_counter = 0

def put_val_file(q, file, e):
    print('Process is alive!')
    val = None
    with open(file, 'a') as _log:
        while (not e.is_set()):
            if(lock.acquire()):
                if(q.qsize()):
                    val = q.get()
                    _log.write(str(val) + ' ')
                lock.release()

def validate_data(args):
    global err_counter
    for index, num in enumerate(prime_nums):
        if (isprime(num)):
            # lock.acquire()
            queue.put(num)
            # lock.release()
        else:
            err_counter += 1
            prime_nums[index] = None

if __name__ == '__main__':

    write_data_process = Process(target=put_val_file, args=(queue, "prime_nums.txt", event))
    write_data_process2 = Process(target=put_val_file, args=(queue, "prime_nums.txt", event))

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
            print(f'len(prime_nums) is: {len(prime_nums)}')
            # validating data
            with cf.ProcessPoolExecutor(max_workers=3) as ex:
                for index, num in enumerate(prime_nums):
                    if (isprime(num)):
                        # lock.acquire()
                        queue.put(num)
                        # lock.release()
                    else:
                        err_counter += 1
                        prime_nums[index] = None

            print(f'queue.qsize() is: {queue.qsize()}')
            print(f'time point 2 is: {time.time() - time1}')

            write_data_process.start()
            write_data_process2.start()

            print(f'err_counter is: {err_counter}')
            clientsocket.close()
            print('Connection closed...')

            # 23.277331590652466
            while(True):
                if(not queue.qsize()):
                    event.set()
                    print(f'time point 3 is: {time.time() - time1}')
                    break
            break
