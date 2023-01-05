class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        
        # Initialize counter.
        count = 0
        for wrd in patterns:

            # If the 'wrd' is in 'word', then increment the counter.
            if wrd in word:
                count += 1

        return count

if __name__ == "__main__":
    patterns = ["a","b","c"]
    word = "aaaaabbbbb"
    sol = Solution()
    ans = sol.numOfStrings(patterns, word)
    # print(ans)