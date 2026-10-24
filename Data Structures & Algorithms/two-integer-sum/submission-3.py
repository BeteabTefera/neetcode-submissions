class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #value, index
        #[2,1,5,3] target = 4 return 1,3
        
        for i, n in enumerate(nums):
            diff = target - n #diff = 4-2 = 2

            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[n] = i
        
