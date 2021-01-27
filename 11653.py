n = int(input())

k = 2
while True:
    if n%k!=0:
        k+=1
    else:
        n = n//k
        print(k)
        k = 2
    if n == 1:
        break