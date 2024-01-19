def binary_search_first(numbers, target):
    """
    think of base case and recursive case
    """
    low, high = 0, len(numbers) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = numbers[middle]
        if guess == target:
            while numbers[middle] == numbers[middle - 1]:
                middle -= 1
            return middle
        if guess > target:
            high = middle - 1
        else:
            low = middle + 1
    return middle 


print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))
# should print 2 (the index of the ‘first’ target number ‘5’ shows up)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
# should print 2 (since it can’t find number 3, return the index of ‘the smallest number larger than 3', that is, the index of the ‘first’ number 5)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3))

print(binary_search_first([1, 2, 5, 5, 5, 6, 7 , 8 , 9 , 10 , 12 , 14 ], 13))