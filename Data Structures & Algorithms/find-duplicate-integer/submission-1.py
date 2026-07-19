class Solution:
    # TREAT IT AS LINKEDLIST CYCLE PROBLEM TO FIND THE BEGINNIGN OF CYCLE
    # FLOYD'S ALGORITHM
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True: # use this pattern for floyd's algorithm
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

