t = int(input())

for i in range(t):
    inputs = input().split()
    n = int(inputs[0])
    k = int(inputs[1])
    if k >= n - 1:
        print(1)
    else:
        print(n)