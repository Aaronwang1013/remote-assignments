def twoSum(nums , target):
    ## use hash table
    temp = {}
    ##j will point to the number(value) and i will point to the index (key)
    for i, j in enumerate(nums):
        if (target - nums[i]) in temp:
            return [temp[target - j] , i]     
        temp[j] = i




print(twoSum([2, 7, 11, 15], 9))