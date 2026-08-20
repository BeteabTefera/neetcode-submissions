class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Understand: 
        array is going to be full of distinct integers, sorted in ascending order 
        another given is target
            goal: if target exist in numbs return its index if not -1

        Match:
        - this is an array problem and indexing, the point is to use binary search
        
        Plan:
            nums = [-1,0,2,4,6,8] target = 4
            nums//2 = [-1,0,2] [4,6,8] 

            total_index = len(nums) - 1 
            mid_val = tot_index//2
            best case is if nums [mid_val] == target 
                return mid value

            left_arr = nums[:mid_val]
            right_arr = nums[mid_val:tot_index]

        Learned:
            - essentially binary search work by modifying the indices not createind new arrays
        '''


        low = 0
        high = len(nums) - 1 #5

        while low <= high:
            mid = (low + high) // 2 #2
            if nums[mid] == target: #nums[mid] == 2
                return mid
        
            if nums[mid] < target:
                low = mid + 1 #now low is 3 nums[3] = 4
            elif nums [mid] > target:
                high = mid -1 
        return -1 