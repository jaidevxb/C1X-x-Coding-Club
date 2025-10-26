inp = input().split()
a = int(inp[0])
b = int(inp[1])

sequence = [b]

while b > a:
    if b % 10 == 1:
        b = (b - 1) // 10
        sequence.append(b)
    elif b % 2 == 0:
        b = b // 2
        sequence.append(b)
    else:
        break

if b == a:
    print("YES")
    sequence.reverse()
    print(len(sequence))
    for i in sequence:
        print(i, end=" ")
else:
    print("NO")
