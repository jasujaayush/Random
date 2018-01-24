import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strmap = collections.defaultdict(list)
        for i in range(len(strs)):
            string = "".join(sorted(strs[i]))
            strmap[string].append(i)
            
        results = [] 
        for key in sorted(strmap, key=lambda k: len(strmap[k])):
            value = strmap[key]
            results.append([strs[i] for i in value])
        return results
                
            
        
