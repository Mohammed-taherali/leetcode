class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev_words = [word[::-1] for word in words]
        rev_str = " ".join(rev_words)

        return rev_str



s = "Let's take LeetCode contest"

sol = Solution()
ans = sol.reverseWords(s)