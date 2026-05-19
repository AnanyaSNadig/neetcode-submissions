class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count = 0

        for n in nums:
            length = 0
            while (n + length) in numSet:
                length += 1
            count = max(count, length)

        return count