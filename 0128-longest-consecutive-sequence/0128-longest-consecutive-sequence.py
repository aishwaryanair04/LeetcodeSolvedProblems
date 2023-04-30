class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        nums=list(set(nums))
        nums=sorted(nums)
        nums.append(0)
        temp=[]
        list1=[]
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                list1.append(nums[i])
            else:
                 list1.append(nums[i])
                 temp.append(list1)
                 list1=[]
        print(temp)
        
        count=0
        for val in temp:
            if len(val)>count:
                count=len(val)
        
        return count
        """
        """
        nums=list(set(nums))
        nums=sorted(nums)
        nums.append(0)
        list1=[]
        temp=[]
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                list1.append(nums[i])
            else:
                list1.append(nums[i])
                temp.append(list1)
                list1=[]
        print(list1)
        
        maxval=0
        for val in temp:
            maxval=max(maxval,len(val))
        return maxval
        """


        nums=sorted(set(nums))
        print(nums)
        nums.append(0)

        i=0
        temp=[]
        list1=[]
        while i<len(nums)-1:
            if nums[i+1]==nums[i]+1:
                list1.append(nums[i])
            else:
                list1.append(nums[i])
                temp.append(list1)
                list1=[]
            i+=1
        print(temp)
        
        maxval=0
        for val in temp:
            maxval=max(len(val),maxval)
        return maxval







     















            

                


        

