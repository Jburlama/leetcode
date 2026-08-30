from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[k]:
                continue
            k += 1
            nums[k] = nums[i]

        return k + 1

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()

print(s.removeDuplicates(nums))
print(nums)
