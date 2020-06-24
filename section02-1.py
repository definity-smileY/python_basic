# Section02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본출력
print('Hello python!')
print("Hello python!")
print("""Hello python! """)
print('''Hello python!''')

print()

# separator 옵션 사용

print('T','E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman','google.com', sep='@')

# end 옵션 사용
print('Welcome to', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# format 사용 [], {}, ()
print('{} and {}'.format('you','me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} are {b}".format(a='You', b='Me' )) # 직관적으로하기

print("%s's favorite number is %d" % ('smile', 7)) #%s : 문자, %d : 정수, %f : 실수 = 제일 정확한 코딩

print("Test1 : %5d, Price : %4.2f" % (776, 6534.123))
print("Test1 : {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test1 : {a: 5d}, price: {b: 4.2f}".format(a=776, b=6534.123))

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n\n\n')
print('\t\t\ttest')
