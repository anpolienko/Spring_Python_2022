class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        N = len(nums)
        for i in range(N - 1):
            expected = target - nums[i]
            if expected in nums_set:
                j = nums.index(expected)
                if j != i:
                    return i, j
                try: 
                    j = nums.index(expected, i + 1)
                except:
                    continue
                return i, j 
