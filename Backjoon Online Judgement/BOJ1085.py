'''
한수는 지금 (x, y)에 있다. 직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고, 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
'''
x, y, w ,h = map(int, input().split())

# x, y가 w, h 밖의 범위인 경우까지 가정할 경우,
# if x < 0 and y < 0: # 3사분면
#     print(((x ** 2) + (y ** 2)) ** 0.5)
# elif x < 0 and y > h: # 2사분면 범위 밖
#     print(((x ** 2) + ((y-h) ** 2)) ** 0.5)
# elif x > w and y > h: # 1사분면 범위 밖
#     print((((x-w) ** 2) + ((y - h) ** 2)) ** 0.5)
# elif x > w and y < 0 : # 4사분면 범위 밖
#     print((((x-w) ** 2) + ((y ** 2)) ** 0.5))
# elif 0<= x <= w and 0<= y <= h: # 범위 안

print(min([(h-y),(x),(w-x),(y)]))