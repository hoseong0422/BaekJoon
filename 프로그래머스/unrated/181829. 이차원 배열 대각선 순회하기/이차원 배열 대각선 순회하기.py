def solution(board, k):
    len_i = len(board)
    len_j = len(board[0])
    answer = 0
    for i in range(len_i):
        for j in range(len_j):
            if i + j <= k:
                answer += board[i][j]
    return answer