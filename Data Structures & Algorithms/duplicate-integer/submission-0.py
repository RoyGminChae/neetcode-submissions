class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        containsList = set() 
        for num in nums:
            if num in containsList:
                return True
            
            containsList.add(num)

        return False