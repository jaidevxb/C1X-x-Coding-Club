inp = input().split()
n = int(inp[0])
t = int(inp[1])

a = []
arr = input().split()
for i in arr:
    a.append(int(i))

pos = 1 

while pos < t:
    pos += a[pos - 1]

if pos == t:
    print("YES")
else:
    print("NO")