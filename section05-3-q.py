# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k in q1.keys():
    if k == "가을":
        print(q1[k])
        break
else:
    print("끝")


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k, v in q2.items():
    if k == "사과" or v == "사과":
        print("사과가있어")
        break
else:
    print("사과가 없어")    
        
    

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

a = 66
if a >= 81:
    print("A")
elif a >= 61:
    print("B")
elif a >= 41:
    print("C")
elif a >= 21:
    print("D")
else:
    print("E")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 12, 6, 18

num = 0
if a > b:
    num = a
if c > b:
    num = c
if c > a:
    num = c
print(num)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'

if int(s[7]) % 2 == 0:
    print("여자입니다")   
else:
    print("남자입니다.")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for l in q3:
    if l == "정":
        continue
    else:
        print(l, end="")
else:
    print("")

q5 = [x for x in q3 if x != '정']
print(q5)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

for i in range(1, 100):
    if i % 2 != 0:
        print(i, end=",")

print("----------------------")

q6 = [x for x in range(1,100) if x % 2 != 0]
print(q6)
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for i in q4:
    if len(i) >= 5:
        print(i, end=",")

print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q5:
    if i.isupper():
        continue
    else:
        print(i, end=",")
print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q6:
    if i.isupper():
        print(i.lower())
    else:
        print(i.upper())

numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)

numbers2 = [x for x in range(1,101)]
print(numbers2)