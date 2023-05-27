class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        count = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                count = 0
            else:
                count += 1
            if count >= len(nums) / 2:
                return nums[i]
            print nums[i],
        return 0
