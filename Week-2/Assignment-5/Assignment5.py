def binary_search_first(numbers, target):
    """
    think of base case and recursive case
    """
    # if target not in number, plus 1 for the target and do it again
    if target not in numbers:
        return binary_search_first(numbers, target+1)
    # if target is larger than the biggest value in list, return None
    if target > numbers[-1]:
        return None
    middle = len(numbers) // 2 
    if numbers[middle] == target:
        # check if there is any identical value
        for i in numbers[:middle]:
            if numbers[i] == target:
                return i
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


# should print 1 (the index of the target number ‘2’)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))
# should print 2 (the index of the ‘first’ target number ‘5’ shows up)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
# should print 2 (since it can’t find number 3, return the index of ‘the smallest number larger than 3', that is, the index of the ‘first’ number 5)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3))
