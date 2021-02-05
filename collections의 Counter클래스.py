from collections import Counter

'''
counter=Counter(a=2, b=3, c=2)
print(counter) #Counter({'b': 3, 'a': 2, 'c': 2})
print(sorted(counter.elements())) #['a', 'a', 'b', 'b', 'b', 'c', 'c']
print('============')
print(Counter(a=2, b=3, c=2)) #Counter({'b': 3, 'a': 2, 'c': 2})
print(sorted(Counter(a=2, b=3, c=2).elements())) #['a', 'a', 'b', 'b', 'b', 'c', 'c']

print(Counter('HAHAha'))   #Counter({'H': 2, 'A': 2, 'h': 1, 'a': 1}) 대소문자 구분
print(sorted(Counter('HAHAha').elements())) #['A', 'A', 'H', 'H', 'a', 'h']

print(Counter(['aa','bb','cc','aa'])) #Counter({'aa': 2, 'bb': 1, 'cc': 1})
print(sorted(Counter(['aa','bb','cc','aa']).elements())) #['aa', 'aa', 'bb', 'cc']


a=[1,1,1,3,3,3]
b=[2,2,3,3,3,3,3]

print(Counter(a)+Counter(b)) #Counter({3: 8, 1: 3, 2: 2})
print(Counter(a)-Counter(b)) #Counter({1: 3}) 2가 -2개이나 음수는 출력되지 않음
print(Counter(a)|Counter(b)) #Counter({3: 5, 1: 3, 2: 2})
print(Counter(a)&Counter(b)) #Counter({3: 3}) 교집합, 3이 3개 겹침

counter=[1,1,1,2,2,3,3,3,4]
print(Counter(counter).most_common()) #[(1, 3), (3, 3), (2, 2), (4, 1)] 아무런 파라미터도 제공하지 않았을 때
print(Counter(counter).most_common(2)) #[(1, 3), (3, 3)]

counter=Counter([1,1,1,2,2,3,3,3,4])
print(counter) #Counter({1: 3, 3: 3, 2: 2, 4: 1})
counter.update({1:4,4:2, 5:1}) #새로운 값까지 업데이트
print(counter) #Counter({1: 7, 3: 3, 4: 3, 2: 2, 5: 1})

counter2=Counter('Aabc')
print(counter2) #Counter({'A': 1, 'a': 1, 'b': 1, 'c': 1})
counter2.update('AAAdD')
print(counter2) #Counter({'A': 4, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'D': 1}) 새로운 문자 까지 포함& 기존 문자 갱신

counter=Counter('Aabc')
print(sorted(counter.elements())) #['A', 'a', 'b', 'c']
'''
counter=Counter('Aabc')
counter2=Counter('AAb')
counter.subtract(counter2)
print(counter) #Counter({'a': 1, 'c': 1, 'b': 0, 'A': -1}) 음수도 나옴










