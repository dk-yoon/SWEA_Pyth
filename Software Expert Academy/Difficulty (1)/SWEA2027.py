'''
주어진 텍스트를 그대로 출력하세요.
'''
n = 5
a = '#'
b = '+'
for i in range (1,n+1):
    print(f'{(i-1)*"+"}#{(n-i)*"+"}')