class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

         dict1={}
        count=0
        for i in nums:
            if i not in dict1.keys():
                dict1[i]=1
                count=1
            else:
                count+=1
                dict1[i]=count
        list1=sorted(dict1.items(), key=lambda x:x[1], reverse=True)
        list
        print(list1)
        for i in range(len(list1)):
            print(list1[i][0])
            
        """
        """
        myset=set(nums)
        dict1={}
        for i in myset:
            if i not in dict1:
                dict1[i]=nums.count(i)
        
        list1=sorted(dict1.items(), key=lambda x:x[1], reverse=True)
        print(list1)

        temp=[]
        for val in list1:
            temp.append(val[0])
        
        print(temp[:k])
        
        return temp[:k]
        """


        dict1={}

        myset=set(nums)
        for val in myset:
            if val not in dict1.keys():
                dict1[val]=nums.count(val)
        print(dict1)

        list1=sorted(dict1.items(), key=lambda x:x[1], reverse=True)

        print(list1)

        temp=[]
        for i in list1[:k]:
            temp.append(i[0])
        
        return temp
        



















        

        
