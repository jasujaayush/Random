class Solution(object):
    def helper(self, s, mem):
        if s in mem:
            return mem[s]
        
        if len(s) == 0:
            mem[s] = [[]]
        else:
            for i,c in enumerate(s):
                if s[:i+1] == s[:i+1][::-1]: #palindrome
                    self.helper(s[i+1:], mem)
                    for res in mem[s[i+1:]]:
                        mem[s].append([s[:i+1]] + res)
                    
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        mem = collections.defaultdict(list)
        self.helper(s, mem)
        return mem[s]
