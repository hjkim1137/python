scores = []

while True:
    score = int(input("성적을 입력하세요(종료 시 '-1' 입력): "))
    if score == -1:
        break
    else:
        scores.append(score)

print('%s' % scores)
# print('%d' % scores)  # TypeError: %d format: a real number is required, not list

# 성적을 입력하세요(종료 시: -1 입력): 800
# 성적을 입력하세요(종료 시: -1 입력): 90
# 성적을 입력하세요(종료 시: -1 입력): -1
# [800, 90]
