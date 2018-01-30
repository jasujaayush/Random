class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        front=0
        back = len(s) -1
        while front < back:
            while front < len(s) and s[front].lower() not in  ['a', 'e', 'i', 'o', 'u']:
                front += 1
            while back >= 0 and s[back].lower() not in  ['a', 'e', 'i', 'o', 'u']:
                back -= 1
            if front < back:
                s[front], s[back]  = s[back], s[front]
            front += 1
            back -= 1
        
        return "".join(s)
                
                
        
        
        
