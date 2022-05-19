class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target:
                    return i, j
