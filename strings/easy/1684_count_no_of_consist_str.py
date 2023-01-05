class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        
        # Initialize the counter.
        t = set(allowed)
        print(t)
        count = 0
        for word in words:

            # Set the flag.
            flag = True
            for char in word:

                # If the char is not in the allowed string, then set the flag to false and break out.
                if char not in allowed:
                    flag = False
                    break

            # Increment the counter.
            if flag:
                count += 1

        return count

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
sol = Solution()
ans = sol.countConsistentStrings(allowed, words)
print(ans)