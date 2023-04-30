class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        if len(s)==len(t):
            myset1=sorted(list(str(s)))
            myset2=sorted(list(str(t)))
            dict1={}
            dict2={}
            count1=0
            count2=0
            for i in myset1:
                if i in dict1.keys():
                    count1+=1
                    dict1[i]+=count1
                else:
                    dict1[i]=1    
            
            for i in myset2:
                if i in dict2.keys():
                    count2+=1
                    dict2[i]+=count2
                else:
                    dict2[i]=1
            return dict1==dict2
        """

        myset1=set(sorted(s))
        myset2=set(sorted(t))
        dict1={}
        dict2={}

        for i in myset1:
            dict1[i]=s.count(i)
        
        for i in myset2:
            dict2[i]=t.count(i)
        
        return dict1==dict2




            


