"""
Task
Реализовать класс - аналог Range
"""

"""
Analogue of range() via Class
:param start: start range value
:param stop:  stop range value
:param step:  increment
:return: <class 'generator'>
"""
class Range:
	def __init__(self, *args):
		len_args = len(args)
		if(len_args and len_args <= 3):
			self.__start = args[0] if len_args >= 2 else 0 
			self.__stop  = args[1] if len_args >= 2 else args[0]
			self.__step  = args[2] if len_args == 3 else 1
			self.__value = None
		else:
			raise TypeError("Input: 1, 2 or 3 argument(s)")

	def __next__(self):
		if self.__start < self.__stop:
			self.__value = self.__start
			self.__start += self.__step
			return self.__value
		else:
			print("iter ended...")
			raise StopIteration

	def __iter__(self):
		return self

# Tests
for iter_obj in [ Range(10), Range(1, 10), Range(5, 50, 10) ]:
	for val in iter_obj:
		print(val)
