class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        count=1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    count+=1
        return count>=2

        """

        myset=set(nums)
        if len(myset) < len(nums):
            return True

        