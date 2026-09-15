class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        if s_len == 0: return True

        s_ptr = 0

        for ch in t:
            if ch == s[s_ptr]:
                s_ptr += 1
                if s_ptr == s_len: return True

        return False
        

sub = "b"
t = "abc"

s = Solution()

print(s.isSubsequence(sub, t))
