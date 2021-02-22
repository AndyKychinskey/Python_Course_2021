"""
Создать класс декоратор (DecorTimeCrit) класса.
Декоратор, который измеряет время выполнения каждого метода,
и печатает предупреждение, только если время выполнения
было больше критического (параметр critical_time)
"""

from time import sleep, time

def benchmark( func, critical_time ):
    def helper( *args, **kwargs ):
        start = time()
        res = func( *args, **kwargs )
        time_mark = time() - start
        if( critical_time ):
            if( time_mark > critical_time ):
                print( "WARNING! {} slow. Time = {} sec.".format( func.__name__, time_mark ) )
        return res
    return helper

def DecorTimeCrit( critical_time = None ):
    def helper( cls, *args, **kwargs ):
        for attr_str in dir( cls ):
            if attr_str.startswith( '__' ):
                continue
            # if attr_str[0:2] == '__':
            #     continue
            attr = getattr( cls, attr_str )
            if callable( attr ):
                decor_attr = benchmark( attr, critical_time )
                setattr( cls, attr_str, decor_attr )
        return cls
    return helper

@DecorTimeCrit(critical_time=0.45)
class Test:
    def method_1(self):
        print('slow method start')
        sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        sleep(0.1)
        print('fast method finish')

t = Test()

t.method_1()
t.method_2()

# slow method start
# slow method finish
# WARNING! method_1 slow. Time = ??? sec.
# fast method start
# fast method finish