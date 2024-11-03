def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        print(i)
        for j in range(1, len(nums)):
            sum1 = nums[i] + nums[j]
            print(sum1)
            if (sum1 == target):
                exit
    exit
    ind = [i, j]
    return ind

x = twoSum([3,3],6)
print(x)