import random

def rolling_dice(pip=6, repeat=1):
    for r in range(1, repeat + 1):
        n = random.randint(1, pip)
        print(pip, "면 주사위 굴린결과", r, " : ", n)


rolling_dice()
rolling_dice(20, 1)
rolling_dice(pip=6, repeat=3)