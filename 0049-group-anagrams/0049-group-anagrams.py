class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        ans = {}
        for i in strs:
            srt = str(sorted(i))
            if srt in ans.keys():
                ans[srt].append(i)
            else:
                ans[srt] = [i]
        return list(ans.values())
        """


        dict1={}

        for val in strs:
            if str(sorted(val)) not in dict1.keys():
                dict1[str(sorted(val))]=[val]
            else:
                dict1[str(sorted(val))].append(val)
        return list(dict1.values())





















