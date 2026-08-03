class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        for num in hashSet:
            if num - 1 in hashSet:
                continue
            
            count = 0
            while num in hashSet:
                num += 1
                count += 1
            
            longest = max(longest, count)

        return longest

        