# Section05-2
# 파이썬 흐름제어 (반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is : ",v1)
    v1 += 1

for v2 in range(10):
    print("v2 is : ", v2)

for v3 in range(1,11):
    print("v3 is : ", v3)

for v4 in range(1, 11, 2):
    print("v4 is : ", v4)

# 1 ~ 100합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 : ', sum1)
print("1 ~ 100 : ", sum(range(1, 101)))
print("1 ~ 100 : ", sum(range(1, 101, 2)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수: range, reverse, enumerate, fillter, map, zip

# 예제1
names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for name in names:
    print("You are : ", name)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Your number", number)

# 예제3
word = "dreams"

for s in word:
    print("word  : ", s)

# 예제4
my_info = {
    "name" : "Kim",
    "age" : 33,
    "city" : "Seoul"
}

for key in my_info:
    print("my_info", key)

for key in my_info.values():
    print("my_info", key)

for key in my_info.keys():
    print("my_info", key)

for key, value in my_info.items():
    print("my_info", key, value)

# 예제5
name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33..")

# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33..")
else:
    print("NOT found 39......")

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("multiply by 2 : ", v * 3)
    print("타입 :", type(v))

name = "Niceman"
print(reversed(name))
print(list(name))
print(tuple(name))
print(list(reversed(name)))


# flag 사용

f = True
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

while f:
    for v in numbers:
        if v == 33:
            print("found : 33!")
            f = False
        print("not found : ", v)

# else 구문 정리 (반복문이 정상적으로 수행 된 경우 else 블럭 수행)
# 예제1

i = 1
while i <= 10:
    print('! : ', i)
    if i == 6:
        break
    i += 1
else:
    print("else block run!")

# 예제2
j = 1
while j <= 10:
    print("j : ", j)
    if j == 11:
        break
    j += 1
else:
    print("else block run!")

# 중첩 for 문 구구단 출력

for i in range(1, 11):
    for j in range(1, 11):
        print("{:4d}".format(i * j), end="")
    print()

# 자료 구조 변환 예제
name = "Niceman"

print("reversed : ", reversed(name))
print("list : ", list(reversed(name)))
print("tuple : ", tuple(reversed(name)))
print("set : ", set(reversed(name))) #순서x
