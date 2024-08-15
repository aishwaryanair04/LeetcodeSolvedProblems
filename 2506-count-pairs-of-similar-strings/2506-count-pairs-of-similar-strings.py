class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        hashmap = {}
        
        for word in words:
            curr = "".join(sorted(set(word)))
            if curr not in hashmap:
                hashmap[curr] = [word]
            else: 
                hashmap[curr].append(word)
        print(hashmap)
        
        count = 0
        for val in hashmap.values():
            k = len(val)
            count += (k*(k-1))//2
        
        return count
            
        
#         count = 0
        
#         for i in range(len(words)):
#             for j in range(i+1,len(words)):
#                 if set(words[i]) == set(words[j]):
#                     count+= 1
                    
#         return count
                    
            
            
        