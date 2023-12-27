from random import randint
a = randint(0, 9)
b = randint(0, 9)
c = randint(0, 9)
# 랜덤 숫자 0~9

while True:
    ball = 0
    strike = 0

    q = int(input("첫번째 숫자를 입력하세요: "))
    w = int(input("두번째 숫자를 입력하세요: "))
    e = int(input("세번째 숫자를 입력하세요: "))

    if (a == q) and (b == w) and (c == e):
        print("게임 종료!")
        break
    if (a == w) or (a == e):
        ball += 1
    if (b == q) or (b == e):
        ball += 1
    if (c == q) or (c == w):
        ball += 1
    if (a == q) or (b == w) or (c == e):
        strike += 1
    print("볼:", ball, "스트라이크:", strike)