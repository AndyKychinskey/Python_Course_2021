# Home work 1, task 1
from math import sqrt
import time

a1 = int( input("Enter your value a1: ") )
a2 = int( input("Enter your value a2: ") )
b1 = int( input("Enter your value b1: ") )
b2 = int( input("Enter your value b2: ") )
c1 = int( input("Enter your value c1: ") )
c2 = int( input("Enter your value c2: ") )

time1 = time.time()
coffs = [ { 'pars': [ a, b, c ], 'root(s)' : None } \
          for a in range(a1, a2+1) for b in range(b1, b2+1) for c in range(c1, c2+1) ]

for i in range( len(coffs) ):
    a, b, c = coffs[ i ]['pars'][0], coffs[ i ]['pars'][1], coffs[ i ]['pars'][2]
    D = b ** 2 - 4 * a * c
    try:
        if D > 0:
            coffs[ i ][ 'root(s)' ] = [ (-b - sqrt( D )) / (2 * a), (-b + sqrt( D )) / (2 * a) ]
        elif D == 0:
            coffs[ i ][ 'root(s)' ] = [ -b / (2 * a) ]
        else:
            coffs[ i ] = None
    except ZeroDivisionError:
        coffs[ i ] = None

coffs = list( filter( None, coffs ) )

time2 = time.time()

for i in range( len(coffs) ):
    print('{} YES {}'.format(coffs[ i ]['pars'], coffs[ i ][ 'root(s)' ]))

print( 'time is {}'.format( time2 - time1 ) )
