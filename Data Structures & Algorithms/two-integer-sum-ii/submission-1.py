class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            value = numbers[i] + numbers[j]
            if value == target:
                return [i + 1, j + 1]
            if value < target:
                i += 1
            if value > target:
                j -= 1

        return []