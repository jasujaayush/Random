	class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0:
            return 0
        
        compressed = []
        prev = ''
        count = 0
        for c in chars:
            if c == prev:
                count += 1
            else:
                if prev != '':
                    if count>1:
                        compressed += [prev] + list(str(count))
                    else:
                        compressed += [prev]
                count = 1
            prev = c
        
        if count>1:
            compressed += [prev] + list(str(count))
        else:
            compressed += [prev]
        
        for i in range(len(compressed)):
            chars[i] = compressed[i]
        del chars[len(compressed):]
        
        return len(chars)
        
