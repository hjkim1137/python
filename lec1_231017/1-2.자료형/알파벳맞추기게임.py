questions = ['tr_in', 'b_s', '_axi', 'air_lane']
answers = ['a', 'u', 't', 'p']

for i in range(len(questions)):
  q='%s에서 밑줄(_)안에 들어갈 알파벳은 ?' %questions[i]
  ans = input(q)
  if ans == answers[i]:
    print('정답입니다!')
  else:
    print('오답입니다!')

# tr_in에서 밑줄(_)안에 들어갈 알파벳은 ?a
# 정답입니다!
# b_s에서 밑줄(_)안에 들어갈 알파벳은 ?u
# 정답입니다!
# _axi에서 밑줄(_)안에 들어갈 알파벳은 ?t
# 정답입니다!
# air_lane에서 밑줄(_)안에 들어갈 알파벳은 ?p
# 정답입니다!