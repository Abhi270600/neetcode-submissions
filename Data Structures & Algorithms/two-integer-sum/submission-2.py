class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashset = {}

        for i in range(len(nums)):
            
            complement = target - nums[i]
            
            if complement in hashset:
                return [hashset[complement], i]

            else:
                hashset[nums[i]] = i
