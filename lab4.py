def sin( x ) :
	sum = x
	term = x
	n = 1
	while sum + term != sum :
		term = (term * (-x) * x) / (2*n * (2*n + 1))
		sum = sum + term
		n = n + 1
	return sum


import random # needed for random number generation

def guess( ) :
	upperbound = 1000
	secret = random.randrange( upperbound )
	# print( f"secret = {secret}" )
	print( "hello, please guess my secret number" )
	print( f"it lies between 0 and {upperbound-1}\n" )

	attempts = 1
	found = 0

	while( found != 1 ) :
		try :
			mess = f"guess {attempts}: "
			inputstring = input( mess ) # Reads input string
			guess = int( inputstring ) # Transforms into int.
		except ValueError :
			print( f"{inputstring} is not a number" )

		if (guess >= 1000 or guess < 0) :
			print( "The input is out of bounds" )
		elif( guess > secret ) :
			print( "The guess is too high" )
		elif ( guess < secret ) :
			print( "The guess is too low" )
		elif ( guess == secret ) :
			print( "The guess is correct" )
			found = 1
		attempts = attempts + 1