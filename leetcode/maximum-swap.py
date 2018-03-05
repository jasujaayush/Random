class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = map(int, str(num))
        digit_index_map = {}
        for i, x in enumerate(digits):
            digit_index_map[x] = i
        
        for i, x in enumerate(digits):
            for y in range(9,x,-1):
                if digit_index_map.has_key(y) and digit_index_map[y] > i: #any larger digit than x later in the sequence
                    y_index = digit_index_map[y]
                    digits[i], digits[y_index] = digits[y_index], digits[i]
                    return int("".join(map(str, digits)))
        return num
        
        
        
