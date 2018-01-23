# Complete the function below.
def getMinInternal(s, minmap):
    if minmap.has_key(s): return minmap[s]   
    #print minmap
    if len(s) == 0: 
        return 0
    elif int(s,16)**0.5 == int(int(s,16)**0.5):
        minmap[s] = 1
        return 1
    
    
    
    ans = -1
    for i in range(1, len(s)+1):
        substr1 = s[:i]
        substr2 = s[i:]
        if int(substr1,16)**0.5 == int(int(substr1,16)**0.5):
            minmap[substr1] = 1
            part2 = getMinInternal(substr2, minmap)
            minmap[substr2] = part2
            if (part2 > 0) and (ans < 0 or ans > (1+part2)):
                ans = 1+part2
    return ans
            
            
    
def getMin(s):
    return getMinInternal(s, {})
