class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        mem = collections.defaultdict(list)
        for i, c in enumerate(S):
            mem[c].append(i)
        
        results = []
        for word in words:
            index = -1
            for j, c in enumerate(word):
                index = bisect.bisect_left(mem[c], index+1)
                #print word, c, index, mem[c]
                if index == len(mem[c]):
                    break
                else:
                    index = mem[c][index]
                    if j==len(word)-1: results.append(word)
        #print results
        return len(results)
                    
                
            
            
        
        
                             
