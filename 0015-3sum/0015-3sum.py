class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]] 
        """
        """
        temp=[]
        for i in range(len(nums)):
            l=i+1
            r=l+1
            while l < len(nums)-1:
                while r < len(nums):
                    if nums[i]+nums[l]+nums[r]==0:
                        if sorted([nums[i],nums[l],nums[r]]) not in temp:
                            temp.append(sorted([nums[i],nums[l],nums[r]]))
                    r=r+1
                l=l+1
                r=l+1

        return temp
        """
        """
        temp=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i!=j!=k:
                        if nums[i]+nums[j]+nums[k]==0:
                            if sorted([nums[i],nums[j],nums[k]]) not in temp:
                                temp.append(sorted([nums[i],nums[j],nums[k]]))

        return temp
        """
        """
        temp=[]
        nums=sorted(nums)
        print(nums)
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            
            while l < r:
                sum=nums[i]+nums[l]+nums[r]
                if sum == 0:
                    if [nums[i],nums[l],nums[r]] not in temp:
                        temp.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    r=r-1
                
                elif sum < 0:
                    l+=1
                else:
                    r-=1
        
        return temp
        """

        nums=sorted(nums)
        temp=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    if [nums[i],nums[j],nums[k]] not in temp:
                        temp.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    
                elif nums[i]+nums[j]+nums[k] < 0:
                    j=j+1
                else:
                    k=k-1

        return temp
















                



    

