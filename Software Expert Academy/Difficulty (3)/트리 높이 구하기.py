import sys
sys.stdin = open('tree_input.txt')

V, E = map(int, input().split())
arr = list(map(int, input().split()))

L = [0] * (V + 1) # 왼쪽 자식
R = [0] * (V + 1) # 오른쪽 자식
P = [0] * (V + 1) # 부모

for i in range(0, E * 2, 2):
    u, v = arr[i], arr[i + 1]

    if L[u] == 0:
        L[u] = v
    else:
        R[u] = v
    P[v] = u

def dfs(v):
    pass

H = 0
def treeHeight(v, h):
    global H
    if v == 0:
        return
    H = max(H, h)
    treeHeight(L[v], h+1)
    treeHeight(R[v], h + 1)

treeHeight(3,0)
print(f'높이 : {H}')