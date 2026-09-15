from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_len = len(nums)
        candidate = 0
        count = 0

        if nums_len == 1: return nums[0]

        for _, num in enumerate(nums):
            if count == 0: candidate = num

            if num == candidate: count += 1
            else: count -= 1

        return candidate
        
nums = [2,2,1,1,1,2,2]

s = Solution()
print(s.majorityElement(nums))
