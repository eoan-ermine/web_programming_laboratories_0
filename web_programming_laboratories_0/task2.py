import math

def main():
	L = [12, 3, 8, 125, 10, 98, 54, 199]

	print(L)
	print(list(map(math.log, L)))

	L[4] = 0
	print(L)
	#print(list(map(math.log, L)))
