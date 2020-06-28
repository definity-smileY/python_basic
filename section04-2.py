# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy"
str2 = "NiceMan"
str3 = ' '
str4 = str('')
print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collections\""
print(escape_str1)
escape_str2 = "Tab\tTab\t"
print(escape_str2)

# Raw String 
raw_s1 = r'C:\nPrograms\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)

# 문자열 연산
str_01 = '*'
str_02 = 'abc '
str_03 = "def"
str_04 = "Niceman"

print(str_01 * 100)
print(str_02 + str_03)
print(str_01 * 3)
print('a' in str_04)
print('f' in str_04)
print('z' not in str_04)

# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))


# 문자열 함수

# a = 'Niceman'
# b = 'orange'

# print(a.islower())
# print(b.endswith('e'))
# print(a.capitalize())
# print(a.replace('Nice', 'good'))
# print(list(reversed(b)))


# 문자열 슬라이싱
a = 'Niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:7])
print(a[0:len(a)])
print(a[:4])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])