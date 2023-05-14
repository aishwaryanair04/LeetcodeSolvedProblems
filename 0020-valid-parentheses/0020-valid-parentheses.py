class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        stack=[]
        dict1={
            '(':')',
            '{':'}',
            '[':']'
        }
        for i in s:
            if i in dict1.keys():
                stack.append(i)
            else:
                if stack==[]:
                    return False
                else:
                    a=stack.pop()
                    if i != dict1[a]:
                        return False
        
        return stack==[]
        """

        stack=[]
        dict1={
            '(':')',
            '{':'}',
            '[':']'
        }

        for x in s:
            if x in dict1.keys():
                stack.append(x)
            else:
                if stack==[]:
                    return False
                else:
                    a=stack.pop()
                    if x!=dict1[a]:
                        return False
        return stack==[]



















                
