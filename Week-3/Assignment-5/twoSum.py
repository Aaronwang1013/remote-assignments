def twoSum(nums , target):
    ## use hash table
    temp = {}
    for i, j in enumerate(nums):
        if (target - nums[i]) in temp:
            return [temp[target - j] , i]     
        temp[j] = i




print(twoSum([2, 7, 11, 15], 9))