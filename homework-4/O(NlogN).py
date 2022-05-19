class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def bin_search(x, array):
            left = 0
            right = len(array) - 1
            while right - left > 1:
                center = (right + left) // 2
                if x < array[center]:
                    right = center
                elif x > array[center]:
                    left = center
                else:
                    return center
            if x == array[right]:
                return right
            elif x == array[left]:
                return left
            return False
        N = len(nums)
        nums_sort = sorted(nums)
        for i in range(N - 1):
            expected = target - nums_sort[i]
            if bin_search(expected,nums_sort[i:]):
                j = nums.index(nums_sort[i])
                k = nums.index(expected)
                if j != k:
                    return j,k
                return j, nums.index(expected, j + 1)
