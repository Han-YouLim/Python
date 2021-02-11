def recurfibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return recurfibo(n-1)+recurfibo(n-2)

print(recurfibo(10))
