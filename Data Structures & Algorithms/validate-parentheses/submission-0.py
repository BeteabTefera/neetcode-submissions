class Solution:
    def isValid(self, s: str) -> bool:
                #using stack to track the brackets
        dic = {')':'(',']':'[','}':'{'} #to gather key values to eliminate multiple conrol flow statements
        stack = []
        #base case is if the str not even
        if len(s)%2 != 0:
            return False
        #check and see if the charachter is an inneie
        for i in s:
            if i in ('(','{','['):
                stack.append(i)
            else:
                if len(stack) ==0 or dic[i] != stack[len(stack)-1]:
                    return False
                else:
                    stack.pop()
        return True if len(stack) == 0 else False