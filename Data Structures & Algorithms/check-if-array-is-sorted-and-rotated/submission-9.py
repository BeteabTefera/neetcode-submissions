class Solution:
    def check(self, nums: List[int]) -> bool:
        #loop through the total array index 1 to len(nums)
        left = [] #space time O(N)
        right = [] #space time O(N)

        for i in range(len(nums)): # run time O(N)
            left.append(nums[i]) # run time O(1)
            right = nums[i+1:] # run time O1)
            print(i,right,left)
            if right + left == sorted(nums):
                return True
        return False
