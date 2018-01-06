def wordpatterninternal(pattern, input, pattern_map):
    print pattern, input, pattern_map
    if len(input) == 0 and len(pattern) == 0:
        print "returning true", pattern_map
        return True
    
    if len(input) == 0 or len(pattern) == 0:
        return False
    
    c = pattern[0]
    if c in pattern_map:
        if input.startswith(pattern_map[c]):
            return wordpatterninternal(pattern[1:], input[len(pattern_map[c]):], pattern_map)
        else:
            return False
                
    for i in range(1, len(input)+1):
        substr = input[:i]
        if substr not in pattern_map.values():
            c = pattern[0]
            new_pattern_map = pattern_map.copy()
            new_pattern_map[c] = substr
            if wordpatterninternal(pattern[1:], input[len(substr):], new_pattern_map):
                print "Here", new_pattern_map
                return True
        
    return False

def  wordpattern( pattern,  input):
        pattern_map = {}
        return int(wordpatterninternal(pattern, input, pattern_map))

wordpattern('abba', "redredredred")
