class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        
        for word in words:
            flag = self.checkPalindrome(word)
            if flag:
                return word
        return ""

    def checkPalindrome(self, word):
        N = len(word)
        front = 0
        back = N-1
        while front<back:
            if word[front] == word[back]:
                front+=1
                back-=1
            else:
                return False
            
        return True

words = ["abc","car","ada","racecar","cool"]

sol = Solution()
ans = sol.firstPalindrome(words)
print(ans)