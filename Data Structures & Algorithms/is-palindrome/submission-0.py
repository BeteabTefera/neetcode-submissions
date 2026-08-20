class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        if s == '':
            return True

        rev_s = ''
        l_str = list(s)

        for i in l_str:
            if i.isalnum():
                rev_s+=i
            else:
                pass
        
        return rev_s == rev_s[::-1]