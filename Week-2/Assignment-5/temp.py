def binary_search_first(numbers, target):
    """
    think of base case and recursive case
    """
    # if target is larger than the biggest value in list, return None
    if target > numbers[-1]:
        return None
    middle = len(numbers) // 2
    # the list will only have one element if no match at all
    if len(numbers) == 1:
        return middle
    if numbers[middle] == target:
        # check if there is any identical value (從middle往後推)
        while numbers[middle] == numbers[middle - 1]:
            middle -= 1
        return middle
    elif numbers[middle] > target:
        numbers = numbers[:middle]
        return binary_search_first(numbers, target)
    elif numbers[middle] < target:
        numbers = numbers[middle + 1:]
        result = binary_search_first(numbers, target)
        # add middle is considering the len of the left part
        # add 1 is considering the start index of the right part
        return result + middle + 1


# print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))
# # should print 2 (the index of the ‘first’ target number ‘5’ shows up)
# print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
# # should print 2 (since it can’t find number 3, return the index of ‘the smallest number larger than 3', that is, the index of the ‘first’ number 5)
# print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3))

# print(binary_search_first([1, 2, 5, 5, 5, 6, 7 , 8 , 9 , 10 , 12 , 14 ], 13))

# print(binary_search_first([1, 2, 5, 5, 5, 6, 7 , 8 , 9 , 10 , 12 , 14 , 16 , 17 , 18], 15))


