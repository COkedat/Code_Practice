"""문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다."""
def DFS(C, V, start, visited):
    if C[start]: # 방문한 적 있다면 무시
        return
    visited.append(start)
    C[start]=True
    for i in V[start]:
        DFS(C, V, i, visited)

    
def BFS(C, V, start, visited):
    q = []
    q.append(start)
    visited.append(start)
    C[start]=True
    while (len(q)!=0):
        print(q)
        x = q.pop(0)
        for i in V[x]:
            if not C[i]:
                q.append(i)
                visited.append(i)
                C[i]=True
    

v, e, s = map(int, input().split(" "))
isvisited = [False for _ in range(v+1)]
vertices = [ [] for _ in range(v+1)]

for i in range(e):
    v1, v2 = map(int, input().split(" "))
    if (v2 not in vertices[v1]): 
        vertices[v1].append(v2)
        vertices[v1].sort()
    if (v1 not in vertices[v2]): 
        vertices[v2].append(v1)
        vertices[v2].sort()
visit = []
DFS(isvisited, vertices, s, visit)
for w in visit:
    print(w, end=" ")
print()


visit = []
isvisited = [False for _ in range(v+1)]
BFS(isvisited, vertices, s, visit)
for w in visit:
    print(w, end=" ")






