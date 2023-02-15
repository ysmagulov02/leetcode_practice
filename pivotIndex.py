class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        list_sum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if leftSum == list_sum - leftSum - nums[i]:
                return i
            else:
                leftSum += nums[i]
        return -1
