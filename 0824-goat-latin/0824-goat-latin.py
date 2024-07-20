class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        words = sentence.split(' ')
        
        for i in range(len(words)):
            if words[i][0] in set('aeiouAEIOU'):
                words[i] = words[i] + 'ma' + ('a'*(i+1))
            else:
                letter = words[i][0]
                words[i] = words[i][1:] + letter + 'ma' + ('a'*(i+1))
        
        return ' '.join(words)
        
        