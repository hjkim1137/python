# 회문은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미
# level, sos, rotator, nurses run
# 회문은 유전자 염기서열 분석에서 많이 사용됨
# n-gram은 빅데이터분석, 검색 엔진에서 많이 사용됨

# https://books.google.com/ngrams


# 회문 판별하기
word = input("단어를 입력하세요:")

is_palindrome = "회문입니다!"
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        is_palindrome = "회문이 아닙니다!"
        break
print(is_palindrome)


# n-gram
# 자연어  처리와 텍스트 분석에서 사용되는 중요한 개념 중 하나.
# 연속된 n개의 아이템(일반적으로 단어, 문자 또는 기호)를 나타내는
# 텍스트 또는 시퀀스 데이터의 부분 문자열

text = 'this is python script'

words = text.split()  # ['this', 'is', 'python', 'script']
print("words:", words)

for i in range(len(words) - 1):  # 3(4-1)
    print(words[i], words[i+1])  # (0,1) (1,2) (2,3)

'''
this is
is python
python script
'''
