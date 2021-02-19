def comparator(elem1, elem2):
    return -1 if elem1 < elem2 else 1 if elem1 > elem2 else 0

def sel_sort(a):
    n=len(a)
    for i in range(0,n-1): #0~n-2
        min_idx=i
        for j in range(i+1, n):
            if comparator(a[j], a[min_idx]) < 0:
                min_idx=j
        a[i], a[min_idx]= a[min_idx], a[i]

d=[2, 4, 5, 1, 3]
sel_sort(d)
print(d) #[1, 2, 3, 4, 5] 내림차순
