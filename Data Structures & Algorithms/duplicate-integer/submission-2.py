class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        M:atch, P:lan, I;mplement
        This is efficient yet i believe there is a better way: 
        len operation is O(N)
        set operation is O(1)

        so total is O(N)
        return len(set(nums)) != len(nums)
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        

        