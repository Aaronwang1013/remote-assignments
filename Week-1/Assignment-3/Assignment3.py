def find_max(numbers):
    if len(numbers) > 0:
        max_number = numbers[0]
    else:
        return None
    for i in range(1, len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
    return max_number


def find_position(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


print(find_max([1, 2, 4, 5]))  # should print 5
print(find_max([5, 2, 7, 1, 6]))  # should print 7
print(find_position([5, 2, 7, 1, 6], 5))  # should print 0
print(find_position([5, 2, 7, 1, 6], 7))  # should print 2
# should print 2 (the first one)
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))
print(find_position([5, 2, 7, 1, 6], 8))  # should print -1

