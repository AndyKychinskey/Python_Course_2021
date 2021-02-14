# Home work 1, task 2
number = int( input("Number range (10-50): ") )
matrix = []

with open( "input.txt" ) as _input:
    data = _input.readlines()
    for line in data:
        matrix.append( [ int( var ) for var in line.split(' ') ] )

total_num_rows, total_num_columns = len( matrix ), len( matrix[ 0 ] )
searched_rows, searched_columns = [], []

for row in range( total_num_rows ):
    for col in range( total_num_columns ):
        if matrix[ row ][ col ] == number:
            searched_rows.append( row )
            searched_columns.append( col )

print( "Rows (index): {}".format( str( set( searched_rows ) )[ 1:-1 ] ) ) 
print( "Columns (index): {}".format( str( set( searched_columns ) )[ 1:-1] ) )
