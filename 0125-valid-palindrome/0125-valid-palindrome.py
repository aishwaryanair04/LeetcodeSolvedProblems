class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        s=str(s.lower())
        s=re.sub("[^0-9a-zA-Z]","",s)
        print(s)
        print(len(s))

        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return False

            l, r = l+1, r-1
        
        return True
        """
        s=re.sub("[^0-9a-zA-Z]","",s)
        s=s.lower()

        l,r=0,len(s)-1

        while l < r:
            if s[l]!=s[r]:
                return False
            l=l+1
            r=r-1
        return True
















        







        