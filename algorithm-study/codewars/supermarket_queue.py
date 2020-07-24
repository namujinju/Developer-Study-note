# sum 배열 값 중 가장 작은 값의 인덱스를 앞에서부터 탐색
# 그 인덱스(i)에 customers.pop(0)를 sum[i]에 더함
# customers가 빈 배열이 될 때까지 반복

def queue_time(customers, n):
    sum = [0 for i in range(n)] #n개의 0을 가진 배열
    
    while customers != []:
        min_index = sum.index(min(sum))
        sum[min_index] += customers.pop(0)
    
    return max(sum)



customers = [2,3,10]
n = 2
print(queue_time(customers, n))