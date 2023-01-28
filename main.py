def longest_substring(x, y, m, n):
    suff = [[0 for k in range(n+1)] for i in range(m+1)]

    result = 0
    for i in range (m+1):
        for j in range (n+1):
            if (i == 0 or j == 0):
                suff[i][j] = 0
            elif (x[i-1]==y[j-1]):
                suff[i][j] = suff[i-1][j-1] +1
                result = max(result, suff[i][j])
            else:
                suff[i][j] = 0

    return result

x = input('enter first string:')
y = input('enter second string:')

print(longest_substring(x,y,len(x) ,len(y)))