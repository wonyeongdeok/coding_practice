'''DFS is Depth-First-Search'''
'''깊이 우선탐색'''

INF = 999999999
# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

for l in graph:
    print(l)
