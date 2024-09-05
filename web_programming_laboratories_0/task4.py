def main():
	numbers = [1, 5, 6, 8, 10, 21, 25, 1, 0, -9, 9]

	k = int(input("Введите целое число от 1 до 10: "))
	assert(k >= 1 and k <= 10)
	print(numbers[k - 1])