class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        
#         l,r = 0, len(nums)-1
        
#         while l <= r:
            
#             if nums[l] == target:
#                 return l
#             if nums[r] == target:
#                 return r
            
#             mid = (l + r)//2
#             if nums[mid] == target:
#                 return mid
#             if target > nums[mid]:
#                 if target < nums[r]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             elif target < nums[mid]:
#                 if target > nums[l]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
            
#         return -1
                
        
#         l,r = 0, len(nums)-1
        
#         while l <= r:
            
#             if nums[l] == target:
#                 return l
#             if nums[r] == target:
#                 return r
            
#             mid = (l + r)//2
#             print(nums[mid])
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 if nums[l] > target:
                    
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             else:
#                 if nums[l] > target:
#                     l = mid + 1
#                 else:
#                     l = mid + 1
        
#         return -1
                
                
                
        
        
        