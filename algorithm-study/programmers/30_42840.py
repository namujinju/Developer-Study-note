def solution(answers):
    
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    lis = [0,0,0]

    for i in range(len(answers)):
        if answers[i] == ans1[i%5]:
            lis[0]+=1
        if answers[i] == ans2[i%8]:
            lis[1]+=1
        if answers[i] == ans3[i%10]:
            lis[2]+=1
    
    return [i+1 for i, value in enumerate(lis) if value == max(lis)]

answers = [1,3,2,4,2]
print(solution(answers))