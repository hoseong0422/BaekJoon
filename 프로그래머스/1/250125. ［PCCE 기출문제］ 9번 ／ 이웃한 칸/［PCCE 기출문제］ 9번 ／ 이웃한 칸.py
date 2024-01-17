def solution(board, h, w):
    answer = 0
    # 위
    center = board[h][w]
    if h != 0:
        if board[h-1][w] == center:
            answer += 1
    # 아래
    if h != len(board) - 1:
        if board[h+1][w] == center:
            answer += 1
    # 좌
    if w != 0:
        if board[h][w-1] == center:
            answer += 1
    # 우
    if w != len(board[0]) - 1:
        if board[h][w+1] == center:
            answer += 1
    return answer