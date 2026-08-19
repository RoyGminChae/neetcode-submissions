class Solution:
    # Kadane's DP Algorithm modification
    # optMax(i) = largest product subarray *ending at i*
    # optMin(i) = smallest product subarray *ending at i*

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        dpMin = dict()
        dpMax = dict()

        def optMin(i):
            if i < 0:
                return 1

            if i in dpMin:
                return dpMin[i]

            dpMin[i] = min(
                nums[i],
                optMin(i - 1) * nums[i],
                optMax(i - 1) * nums[i]
            )

            return dpMin[i]

        def optMax(i):
            if i < 0:
                return 1    
        
            if i in dpMax:
                return dpMax[i]

            dpMax[i] = max(
                nums[i],
                optMin(i - 1) * nums[i],
                optMax(i - 1) * nums[i]
            )

            return dpMax[i]

        return max(optMax(i) for i in range(n))
            



        