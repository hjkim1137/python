import random
import time

w = ['red', 'yellow', 'blue', 'white', 'purple', 'orange', 'black']

n = 1  # 통과한 문제 개수
print("타자게임이 준비되면 enter를 치세요.")
input()

startTime = time.time()
q = random.choice(w)
while n <= 5:  # 5문제를  맞힐때까지 지속함
    print("*문제", n)
    print(q)
    x = input()
    if q == x:
        print("[통과!]")
        n = n+1
        q = random.choice(w)
    else:
        print("[오타! 다시도전]")
endtime = time.time()
et = endtime - startTime
et = format(et, ".2f")
print("타자시간:", et, "초")
