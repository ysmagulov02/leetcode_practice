class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = list()
        curr_sum = 0
        for i in range(len(nums)):
                curr_sum += nums[i]
                ans.append(curr_sum)
        return ans
