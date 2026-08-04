class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            
            # skip dups for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if value < 0:
                    j += 1
                elif value > 0: 
                    k -= 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                    # Skip duplicate second values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate third values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res

            
