class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        record=[]

        for i in range(len(operations)):
            print(record)
            x=operations[i]
            if x=='+':
                a=record.pop()
                b=record.pop()
                record.append(b)
                record.append(a)
                record.append(int(a)+int(b))
            elif x=='D':
                a=record.pop()
                record.append(a)
                record.append(int(a)*2)
            elif x=='C':
                record.pop()
            else:
                record.append(int(x))
        
        score=0
        for val in record:
            score+=int(val)
        
        return score

        
        


