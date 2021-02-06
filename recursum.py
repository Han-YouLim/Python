def recursum(n):
    if n==1:
        return 1
    sum=n+recursum(n-1)
    return sum

def recurmax(li,length):
    if length==1:
        return li[0]
    maxnum=recurmax(li, length-1)
    if maxnum>=li[lenght-1]:
        return maxnum
    else:
        return li[lenght-1]
    
print(recursum(10))
temp = [33, 44, 5, 66, 139, 90, 45, 23]
print (recurmax(temp, len(temp)))

