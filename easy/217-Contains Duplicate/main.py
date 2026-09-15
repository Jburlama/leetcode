from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(i)
        return False


nums = [1,1,1,3,3,4,3,2,4,2]

s = Solution()

print(s.containsDuplicate(nums))
