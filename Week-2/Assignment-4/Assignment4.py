def count(input):
    count_dict = {}
    for i in range(len(input)):
        count_dict[input[i]] = 0
    for i in range(len(input)):
        if input[i] in count_dict:
            count_dict[input[i]] += 1
    return count_dict


# your code here
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    count_dict = {}
    for i in range(len(input)):
        count_dict[input[i]['key']] = 0
    for i in range(len(input)):
        if input[i]['key'] in count_dict:
            count_dict[input[i]['key']] += input[i]['value']
    return count_dict


# your code here
input2 = [
    {'key': 'a', 'value': 3},
    {'key': 'b', 'value': 1},
    {'key': 'c', 'value': 2},
    {'key': 'a', 'value': 3},
    {'key': 'c', 'value': 5}
]
print(group_by_key(input2))  # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
