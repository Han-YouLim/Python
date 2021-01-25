import re
# s="$$abc$$ABC"
# print(s.lower())
# s=re.sub('[^a-z0-9]', '', s) #regular expression
# print(s)

# logs=["dig1 8 1 5","let1 art can"]
# #print(logs.split()) #AttributeError: 'list' object has no attribute 'split'
# for log in logs:
#     print(log.split()) #['dig1', '8', '1', '5']    ['let1', 'art', 'can']
#     print(log) #dig1 8 1 5
#
# def func(x):
#     return x.split()[1], x.split()[0]
#
# s=['2 a','1 b', '4 c', '1 a']
# s.sort(key=func)
# print(s)

# # 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# # 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.
# e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
# f = sorted(e, key = lambda x : (x[0], -x[1]))
# # f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]

# a = 'abcdef\nabc'
# print(a)
#
# b = r'abcdef\nabc123$$'
# print(b) #abcdef\nabc123$$
# b=re.sub(r'[^\w]','',b)
# print(b) #abcdefnabc123 #문자나 숫자가 아니면 ''로 바뀜
# import collections
# anagrams = collections.defaultdict(list) #list 명시 안해주면 KeyError: 'aet' 라는 에러남 => efault_factory 는 defaultdict의 초기값을 지정하는 인자이다.
# # default_factory 인자를 넣어주지않으면 기본 딕셔너리와 마찬가지로 KeyError Exception 에러가 난다. (default_factory는 list(), int(), set() 등이 있다. 예시는 다음 블록에.
# strs=["eat", 'tea', 'tan', 'ate', 'nat', 'bat']
# for word in strs:
#     # 정렬하여 딕셔너리에 추가
#     anagrams[''.join(sorted(word))].append(word) #
# print(anagrams) #defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})


# # 예제(2-1) - default_factory를 지정한 경우
import collections
# def default_factory():
#     return 'null'
# ex2 = collections.defaultdict(default_factory, a=1, b=2)
# print(ex2)
# print(ex2['c'])
'''
결과
defaultdict(<function default_factory at 0x10ab50c80>, {'b': 2, 'a': 1})
null
'''

# ex_list = collections.defaultdict(list, a=[1,2], b=[3,4])
# print(ex_list)
# print(ex_list['c'])
# ex_list['c'].append([1,2,3,4])
# print(ex_list) #defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3, 4], 'c': [[1, 2, 3, 4]]})
'''
결과
defaultdict(<class 'list'>, {'b': [3, 4], 'a': [1, 2]}) #리스트를 value로!
[]
defaultdict 생성자에 list 함수를 넘겼기 때문에, 사전에 어떤 글자가 키(key)로 존재하지 않는 경우, 해당 키에 대한 기본값을 비어있는 리스트(empty list)로 세팅해줍니다.
append를 사용하여 value리스트에 값을 추가.
ex)ex_list[key].append(value) #이때 ex_list는 defaultdict
'''
# # 3-2. set
# ex_set = collections.defaultdict(set, a={1,2}, b={3,4})
# print(ex_set)
# print(ex_set['c'])
'''
결과
defaultdict(<class 'set'>, {'b': {3, 4}, 'a': {1, 2}}) #집합을 value로!
set()
defaultdict 생성자에 list 함수 대신에 set 함수를 넘기고, append 함수 대신에 add 함수를 이용해서 단어를 넘기면 됩니다.
defaultdict[key].add(value)
'''
# # 3-3. int
# ex_int = collections.defaultdict(int, a=1, b=2)
# print(ex_int)
# print(ex_int['c'])
'''
결과
defaultdict(<class 'int'>, {'b': 2, 'a': 1})
0
defaultdict 클래스의 생성자로 int 함수를 넘긴 이유는 int()는 0을 리턴하기 때문입니다. 람다 함수를 활용해서 다음과 같이 int 함수 대신에 lambda: 0를 넘겨도 동일하게 작동을 합니다.
defaultdict[key] += value
'''
# a="able"
# print(a.split('b')) #list로 반환 key=b일 때의 결과,['a', 'le']
# print(a.split('b')[1]) #le
# print(a) #able split은 원본에 손대지x

