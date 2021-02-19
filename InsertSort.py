def ins_sort(a): #오름차순
    n=len(a)
    for i in range(1, n): #idx:1~n-1(끝)
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
            print(a, key)
        a[j+1]=key
        

d=[2, 4, 5, 1, 3]
ins_sort(d)
print(d)
        
