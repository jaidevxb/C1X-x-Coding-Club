from collections import deque

n = int(input())
manager = [int(input()) for i in range(n)]
children = [[] for i in range(n)]
roots = []

for i in range(n):
    if manager[i] == -1:
        roots.append(i)
    else:
        children[manager[i]-1].append(i)

max_depth = 0
queue = deque()

for r in roots:
    queue.append((r, 1))

while queue:
    emp, d = queue.popleft()
    max_depth = max(max_depth, d)
    for ch in children[emp]:
        queue.append((ch, d+1))

print(max_depth)
