def sosu(sosu_n):
    k = int(sosu_n)
    n = 2
    while True:
        if k == n:
            c = 1
            break
        elif k%n != 0:
            n+=1
        else:
            break
            
    
while True:
    c = 0
    count = 0
    n = int(input())
    for i in range(n+1, (2*n)+1):
        c = 0
        sosu(i)
        if c == 1:
            count +=1
    print(count)



