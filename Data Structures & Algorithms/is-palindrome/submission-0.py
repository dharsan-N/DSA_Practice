class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=""
        for x in s:
            if x.isalnum():
                l+=x.lower()
        print(l)
        if l==l[::-1]:
            return True
        else:
            return False
