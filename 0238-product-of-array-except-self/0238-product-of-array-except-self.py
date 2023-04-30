class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         final_list=[]
#         for i in range(len(nums)):
#             prefix=[]
#             postfix=[]
#             temp_list=[]
#             prefix.append(nums[:i])
#             postfix.append(nums[i+1:])
#             print(prefix)
#             print(postfix)
#             temp_list=prefix[0]+postfix[0]
#             print("temp_list: ", temp_list)
#             val=1
#             for x in temp_list:
#                 val=val*x
#             print(val)
#             final_list.append(val)
#             print(final_list)
        
#         return final_list

        prefix = []
        preNum = 1
        for i in range(len(nums)):
            prefix.append(preNum)
            preNum *= nums[i]
        print("prefix 1st loop: ", prefix)
        postNum = 1
        # for i in range(len(prefix)-1,-1,-1):
        for i in reversed(range(len(prefix))):
            prefix[i] *=  postNum
            postNum *= nums[i]
        print("prefix 2nd loop: ", prefix) 
        return prefix


                    
            
            
            
            
            
            
            
        
        