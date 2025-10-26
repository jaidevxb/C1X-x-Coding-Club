t = int(input())

for i in range(t):
    n = int(input())
    row1 = input()
    row2 = input()

    top = bottom = 0  
    top = 1 

    for j in range(n):
        new_top = new_bottom = 0
        if top:
            if row1[j] == '0':
                new_top = 1
            if row2[j] == '0':
                new_bottom = 1
        if bottom:
            if row2[j] == '0':
                new_bottom = 1
            if row1[j] == '0':
                new_top = 1
        top, bottom = new_top, new_bottom

    if bottom == 1:
        print ("YES")
    else:
        print("NO")
