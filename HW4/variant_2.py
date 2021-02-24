"""
Task
Реализовать класс - аналог Range
"""

# analogue of range() via function
def _range( *args ):
	"""
	Analogue of range() via function
	:param start: start range value
	:param stop:  stop range value
	:param step:  increment
	:return: list of values
	"""
	len_args = len(args)
	if( len_args and len_args <= 3 ):
		start, stop, step, res = 0, 0, 1, []
		if len_args == 3:
			start, stop, step = args[ 0 ], args[ 1 ], args[ 2 ]
		elif len_args == 2:
			start, stop = args[ 0 ], args[ 1 ]
		else:
			stop = args[ 0 ]
		while( start < stop ):
			res.append( start )
			start += step
		return res
	raise TypeError("Input: 1, 2 or 3 argument(s)")
# Test
print(_range(10))
print(_range(1,10))
print(_range(1,10,2))
# print(_range()) # raise TypeError

# analogue of range() via function
def _range_generator( *args ):
	"""
	Analogue of range() via function
	:param start: start range value
	:param stop:  stop range value
	:param step:  increment
	:return: <class 'generator'>
	"""
	start, stop, step, len_args = 0, 0, 1, len(args)
	if len_args == 3:
		start, stop, step = args[ 0 ], args[ 1 ], args[ 2 ]
	elif len_args == 2:
		start, stop = args[ 0 ], args[ 1 ]
	elif len_args == 1:
		stop = args[ 0 ]
	else:
		raise TypeError("Input: 1, 2 or 3 argument(s)")
	#print("start = {}, stop = {}, step = {}".format(start, stop, step))
	def result():
		nonlocal start
		while( start < stop ):
			yield start
			start += step
	return result()
# Test
my_gen = _range_generator(5)
print(type(my_gen))
for val_from_gen in my_gen:
	print( val_from_gen )
