iclass Solution(object):
    def helper(self, s, mem):
        if s in mem:
            return mem[s]
        
        if len(s) == 0:
            mem[s] = [[]]
        else:
            for i in range(len(s)-1, -1, -1):
                if s[:i+1] == s[:i+1][::-1]: #palindrome
                    self.helper(s[i+1:], mem)
                    for res in mem[s[i+1:]]:
                        mem[s].append([s[:i+1]] + res)
                    break
            
            if len(mem[s][0]) > 2:
                for i,c in enumerate(s):
                    if s[:i+1] == s[:i+1][::-1]: #palindrome
                        self.helper(s[i+1:], mem)
                        temp = []
                        for res in mem[s[i+1:]]:
                            temp.append([s[:i+1]] + res)
                        #print s, temp
                        if len(temp[0]) < len(mem[s][0]):
                            mem[s] = temp
                    
    
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = collections.defaultdict(list)
        self.helper(s, mem)
        print mem[s]
        return len(mem[s][0]) - 1
