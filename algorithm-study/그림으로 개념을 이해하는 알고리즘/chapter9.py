from numpy import zeros

# 최장 공통 부분 문자열

def longest_common_substring(s1, s2):
    max_value = 0
    cell = zeros((len(s1),len(s2)))

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                cell[i][j] = cell[i-1][j-1] + 1

                if cell[i][j] > max_value:
                    max_value = cell[i][j]
            else:
                cell[i][j] = 0
    
    return int(max_value)


s1 = "blue"
s2 = "clues"

print(longest_common_substring(s1,s2))

# 최장 공통 부분열

def longest_common_subsequence(s1, s2):
    cell = zeros((len(s1)+1,len(s2)+1))
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    
    return int(cell[-2][-2])


s1 = "plane"
s2 = "apple"
print(longest_common_subsequence(s1, s2))