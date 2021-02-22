"""
Создать класс декоратор (DecorTimeCrit) класса.
Декоратор, который измеряет время выполнения каждого метода,
и печатает предупреждение, только если время выполнения
было больше критического (параметр critical_time)
"""

"""
Note.
I have not found nice task's root, so I have remastered code in the end.
"""

from time import sleep, time


class DecorTimeCrit:
    def __init__(self, cls, *args, **kwargs):
        self.__cls = cls(*args, **kwargs)

    def e_time(self, func, critical_time, *args, **kwargs):
        start = time()
        func(*args, **kwargs)
        delta_time = time() - start
        if(delta_time > critical_time):
            print("WARNING! {} slow. Time = {} sec.".format(func.__name__, delta_time))

    def __call__(self, critical_time = None):
        def helper(*args, **kwargs):
            for attr_str in dir(self.__cls):
                if attr_str.startswith('__'):
                    continue
                attr = getattr(self.__cls, attr_str)

                if callable(attr):
                    self.e_time(attr, critical_time, *args, **kwargs)

        return helper

# @DecorTimeCrit(critical_time = 0.45)
class Test:
    def method_1(self):
        print('slow method start')
        sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        sleep(0.1)
        print('fast method finish')

# testing class Test
test = DecorTimeCrit(Test)(critical_time = 0.45)
test()

"""
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
"""
