class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 2
        for i in range(3, n):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr + prev

steps = 5
s = Solution()
print(s.climbStairs(steps))
