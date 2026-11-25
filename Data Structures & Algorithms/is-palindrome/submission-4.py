class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = [ch for ch in s.lower() if 'a' <= ch <= 'z' or '0' <= ch <= '9']
        
        i = 0
        j = len(s2) - 1

        while(i < j):
            if(s2[i] != s2[j]):
                return False
            i += 1
            j -= 1

        return True
        