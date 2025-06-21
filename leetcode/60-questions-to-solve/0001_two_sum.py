class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for idx1 in range(len(nums)):
            for idx2 in range(idx1 + 1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    result.append(idx1)
                    result.append(idx2)
                    break

        return result
