class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = set()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if value < 0:
                    j += 1
                elif value > 0: 
                    k -= 1
                else:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        
        output = []
        for x, y, z in triplets:
            output.append([x, y, z])
        
        return output

            
