def binary_search_position(numbers, target):
    """
    think of base case and recursive case
    """
    if not numbers:
        return None
    if target > numbers[-1]:
        return None
    middle = len(numbers) // 2
    if numbers[middle] == target:
        return middle
    elif numbers[middle] > target:
        numbers = numbers[:middle]
        return binary_search_position(numbers, target)
    elif numbers[middle] < target:
        numbers = numbers[middle + 1:]
        result = binary_search_position(numbers, target)
        # add middle is considering the len of the left part
        # add 1 is considering the start index of the right part
        return result + middle + 1


# print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0 print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
print(binary_search_position([1, 2, 5, 6, 7], 1))
print(binary_search_position([1, 2, 5, 6, 7], 6))
