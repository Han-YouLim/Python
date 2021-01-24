# print([n *2 for n in range(1, 10+1) if n % 2 == 1]) #list_comprehension
# def get_num() -> int: #type hint
#     num=0
#     while num<100:
#         num+=1
#         yield num #generater operation example 1. yield
#
# g= get_num()


# for i in range(1, 99+1):
#     print(next(g)) #1~99 print
#
# print("******************")


# b=range(100) #generater operation example 2. range
# print(len(b))
# for i in range(0, 99+1):
#     print(b[i]) #index=> 0~99
#
# print("******************")


# a= ['z', 'x'] #if a is Integer list,
# print(', '.join(a)) #it doesn't work
# print(f'{a[0]}ero: {a[1]}') #zero: x
#


# a=b=1 #a는 b가 참조하는 값인 1을 참조.
# print(a is b) #True => int type variable is immutable object
# print(id(a)) #variable a and variable b refer to a same value
# print(id(b))
# a=2
# print(id(a)) # id of a 는 달라진다. 다른값을 참조하게 되었다는 뜻.
# print(a is b)
# print(b) #valuable b refer to the same value(id)


# list_ex=[1, 3, '안녕']
# list_ex2=[2, 3, '안녕']
# print(list_ex[2] is list_ex2[2]) #True 각 다른배열에서 같은 값 '안녕'을 참조하고 있음(id 동일)
# print(id(list_ex[0])) #2504341612848
# print(list_ex[1] is list_ex2[1]) #True
# print(True ==1) #True the value is same between 1 and True
# print(id(True)) #140706398435432
# print(id(1)) #2504341612848 the id of one(1) located in memery is not same with the id of True


# import collections
# a=[1,2,3,4,4,5,2,6,1,1,1,1,1,1]
# b=collections.Counter(a)
# print(b) #Counter({1: 7, 2: 2, 4: 2, 3: 1, 5: 1, 6: 1}) dict이 Counter로 한번더 wrapping => type is <class 'collections.Counter'>
# print(b.most_common(2)) #[(1, 7), (2, 2)]
# for i in b.most_common(2):
#     print(i) #(1, 7)   (2, 2) tuple 출력
#     print(i[1]) #7 2로 개수가 출력됨 (Counter로 래핑된 딕셔너리상 value)
#     print(i[0]) #1 2로 값이 출력됨(Counter로 래핑된 딕셔너리상 key)

