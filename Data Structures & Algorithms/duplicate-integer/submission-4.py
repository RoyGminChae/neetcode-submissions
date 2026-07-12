class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appears_once = set()
        for num in nums:
            if num not in appears_once:
                appears_once.add(num)
            else:
                return True
            
        return False