"""
Клиент
1. генерирует простые числа в диапазоне от 0 до 2000000 (их всего 148933)
2. отправляет эти числа на сервер
"""
import time
import socket
import communication

lim_high = 2000000
prime_nums = None

def primes(n):
    """
    Returns a list of primes < n
    https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
    """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

t1 = time.time()

# prime nums
prime_nums = primes(lim_high)
t2 = time.time()
print(f'time is: {t2 - t1}')

# data handling
client = socket.socket()
client.connect((socket.gethostname(), 56+13))
t3 = time.time()
communication.sendMsg( prime_nums, client )
t4 = time.time()
print(f'time is: {t4 - t3}')
client.close()
