from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1

        while end > start:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
input = ["H","a","n","n","a","h"]

s = Solution()
s.reverseString(input)

print(input)
