# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
# print(d[3])
# print(d[-2])
# print(d[0]+d[1])
# print(e[2][1])
# print(e[-1][-2])
print('#=======#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][1][4]) 
print('e - ', list(e[-1][1])) 

# 슬라이싱
print('#======#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])
# print(d[0:3])
# print(e[2][1:3])


# 리스트 연산
print('#=======#')
print('c + d -', c + d)
print('c * d -', c * 3)
# print("c[0] + 'hi' -",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))
# print(c + d)
# print(c * 3)
# print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
print('#=======#')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c -', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c)
# c[0] = 77
# print(c)

# c[1:2] = [100, 1000, 10000]
# print(c)
# c[1] = ['a', 'b', 'c']
# print(c)

# del c[1]
# print(c)
# del c[-1]
# print(c)
# print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('#==========#')
print('a - ', a)
a.append(6)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(5))
a.insert(2, 7)
print('a - ', a)
a.reverse()
a.remove(1)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))



# print(y)
# y.append(6)
# print(y)
# y.sort()
# print(y)
# y.reverse()
# print(y)
# y.insert(2,7)
# print(y)
# y.remove(2)
# y.remove(7)
# print(y)
# y.pop()
# print(y) #LIFO
# ex = [88, 77]
# # y.append(ex)
# y.extend(ex)
# print(y)

# 삭제 : del, remove, pop

# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1,)
c = (1,2,3,4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)
print()

# 튜플 함수

z = (5,2,1,3,1)

print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))