def longestOneSubString(inputString):
    iterator = 0
    max_length = 0
    count = 0
    for iterator in range(len(inputString)):
        if inputString[iterator] == '1':
            count += 1
        else:
            max_length = max(max_length, count)
            count = 0
    max_length = max(max_length, count)        
    return max_length


def longestOneSubStringWithOneDeletion(inputString):
    iterator = 0
    max_length = 0
    length_list = []
    count_ones = 0
    count_zeros = 0
    while iterator < len(inputString):
        if inputString[iterator] == '1':
            while iterator < len(inputString) and inputString[iterator] == '1':
                iterator += 1
                count_ones+=1
            length_list.append(('1', count_ones))  
            max_length = max(max_length, count_ones)        
            count_ones = 0
        else:
            while iterator < len(inputString) and inputString[iterator] == '0':
                iterator += 1
                count_zeros +=1
            length_list.append(('0', count_zeros))    
            count_zeros = 0  
    print length_list  #tamporary check      
    
    twoCount = 0
    for i in range(len(length_list)):
        l = length_list[i]
        if l[0] == '0' and l[1] <= 1 and (i-1) >= 0 and (i+1) < len(length_list):
            twoCount = length_list[i-1][1] + length_list[i+1][1]
            max_length = max(max_length, twoCount)
            
    return max_length

print longestOneSubStringWithOneDeletion("10100111")
print longestOneSubStringWithOneDeletion("1111")
print longestOneSubString("110101001")

# 
# Your previous Plain Text content is preserved below:
# 
# Given a binary string, find the length of the longest string of conseuctive 1's
# 
# inputString = "00000000001111111111111100001110101" #sample input
# 
# left_index = 0
# right_index = 0
# 
# while



