def two_sum(nums, target):
    found = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]

            if (sum == target):
                found=[i,j]

    if(len(found)>0):
      print(found)
      return found
    else:
        print([-1,-1])
        return [-1,-1]

two_sum([1, 4, 6, 10], 11)