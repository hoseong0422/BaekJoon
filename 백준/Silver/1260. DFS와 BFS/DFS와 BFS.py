def dfs(current_node):
    """
    깊이 우선 탐색 (DFS)
    current_node: 현재 방문 중인 노드
    """
    dfs_result.append(current_node) # 방문 순서 기록
    visited[current_node] = True    # 방문 처리

    for next_node in graph[current_node]:
        if not visited[next_node]:
            dfs(next_node)

def bfs(start_node):
    """
    너비 우선 탐색 (BFS)
    start_node: 탐색 시작 노드
    """
    queue = [] # 방문 대기 큐 생성

    queue.append(start_node)
    bfs_result.append(start_node)
    visited[start_node] = True

    while queue:
        current_node = queue.pop(0) # 큐의 앞에서 하나 꺼내기

        for next_node in graph[current_node]:
            if not visited[next_node]:
                queue.append(next_node) # 다음 탐색 대상 큐 추가
                bfs_result.append(next_node)
                visited[next_node] = True


# N: 정접, M: 간선, V: 시작 정점
N, M, V = map(int, input().split())

# 정점 번호와 인덱스를 일치시키기 위해서 N + 1 범위로 생성 (인덱스 0번은 버리는 공간)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a) # 양방향 간선이므로 a에는 b, b에는 a 추가

# 문제 조건: 방문 순서를 오름차순으로 맞추기
for i in range(N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
dfs_result = []
dfs(V)

visited = [False] * (N + 1)
bfs_result = []
bfs(V)

print(*dfs_result)
print(*bfs_result)
