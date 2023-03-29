def binary_search(list, item):
	low  = 0
	high = len(list) - 1

	while low <= high:
		mid = (low+high)//2
		guess = list[mid]

		if guess == item:
			return mid
		elif item < guess:
			high = mid - 1
		elif item > guess:
			low = mid + 1
	return None

numbers = [1, 3, 5, 7, 9]
print(binary_search(numbers, 4))
