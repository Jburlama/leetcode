class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        count = {}
        for i, num in enumerate(s):
            if num not in count:
                count[num] = 1
                continue
            count[num] += 1

        for i, num in enumerate(t):
            if num not in count: return False
            count[num] -= 1
            if count[num] < 0: return False

        return True
        

s1 = "anagram"
s2 = "nagaram"

s = Solution()

print(s.isAnagram(s1, s2))
