def leet(nums):
    k = 0
    newList = []
    for i in range(len(nums) - 1):
        if nums[i] not in newList:
                newList.append(nums[i])
    return len(newList), newList

nums = [1,1,1,1, 1, 2, 3, 3]
print(leet(nums))


# leetcode

class Solution(object):

    def removeDuplicates(self, nums):
        newList = []

        for num in nums:
            if num not in newList:
                newList.append(num)

        for i in range(len(newList)):
            nums[i] = newList[i]

        return len(newList)
