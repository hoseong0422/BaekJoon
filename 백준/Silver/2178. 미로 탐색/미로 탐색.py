from collections import deque

def shortest_path_bfs(start_row: int, start_col: int, end_row: int, end_col: int) -> int:
    """
    BFS로 미로(2178) 최단 거리(이동 칸 수)를 구한다.
    - maze[r][c] == 1: 이동 가능
    - maze[r][c] == 0: 벽
    - dist[r][c] : (start_row, start_col)에서 (r, c)까지의 이동 칸 수(거리)
    """

    # dist를 0으로 두면 "아직 방문 안 함"을 의미하게 할 수 있음
    dist = [[0] * M for _ in range(N)]
    queue = deque()

    # 시작점 초기화
    queue.append((start_row, start_col))
    dist[start_row][start_col] = 1  # 시작 칸도 1칸으로 카운트(문제 조건에 맞춤)

    # 상/하/좌/우 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col = queue.popleft()

        # 도착 지점에 도달하면 최단거리 확정 (BFS 특성)
        if (row, col) == (end_row, end_col):
            return dist[end_row][end_col]

        # 인접한 4방향 탐색
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc

            # 1) 범위 안인지
            # 2) 길(1)인지
            # 3) 아직 방문 안 했는지(dist == 0)
            if (
                0 <= next_row < N and 0 <= next_col < M
                and maze[next_row][next_col] == 1
                and dist[next_row][next_col] == 0
            ):
                dist[next_row][next_col] = dist[row][col] + 1
                queue.append((next_row, next_col))

    # 문제 조건상 항상 도달 가능하다고 보는 풀이가 많지만,
    # 혹시 모를 경우를 대비해 도달 불가면 0(또는 -1) 리턴
    return 0


# 입력
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

# (0,0) -> (N-1, M-1)
answer = shortest_path_bfs(0, 0, N - 1, M - 1)
print(answer)