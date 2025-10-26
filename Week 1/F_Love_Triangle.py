n = int(input())
arr = input().split()

f = []
for i in arr:
    f.append(int(i))

found = False

for i in range(n):
    A = i + 1        
    B = f[i]            
    C = f[B - 1]        
    if f[C - 1] == A:   
        found = True
        break

if found == 1:
    print("YES")
else:
    print("NO")
