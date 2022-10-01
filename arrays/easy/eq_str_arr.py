class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
    #  for w in word1:
    #     word += w 
    #     print(word)
        w1 = ""
        w2 = ""
        for wo1 in word1:
            w1 += wo1

        for wo2 in word2:
            w2 += wo2

        if w1 != w2:
            return False
        else:
            return True

word1 = ["ab", "c"]
word2 = ["a", "bc"]

sol = Solution()
ans = sol.arrayStringsAreEqual(word1, word2)
# print(ans)

def gen():
    i = 0
    while True:
        yield i
        i += 1


obj = gen()

for i in obj:
    print(i, end=" ")