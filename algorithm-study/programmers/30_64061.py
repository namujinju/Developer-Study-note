def solution(board, moves):
    ans = 0
    va = [0, 0] # va = vaguni
    n = 0
    for i in moves:
        
        for n in range(len(board)):
            k = board[n][i-1]

            if k != 0:
                va.append(k)
                board[n][i-1] = 0
                
                if va[-1] == va[-2]:
                    va.pop(-1)
                    va.pop(-1)
                    ans+=2
                break

    return ans


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
    