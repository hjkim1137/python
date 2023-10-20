# 클래스: 변수와 함수를 모아놓은 것
# 클래스명은 반드시 대문자로 시작한다

# 클래스의 구성
# • 클래스 : 속성과 동작을 가짐
# 속성 : 객체를 구성하는 데이터 -> 변수
# 동작 : 속성에 대해 어떤 기능을 수행하는 함수 -> 매서드
# 생성자 : 생성시 초기화 작업을 수행, 생략 가능
# 소멸자 : 소멸시 종료 작업을 수행, 생략 가능

# • 개체 생성
# 변수이름 : 클래스명()

# 클래스 정의
# class 클래스명:
# 변수 A
# 변수 B
# …
# def 메소드명():
# 문장1
# 문장2
# …
# def 메소드명():
# 문장10
# 문장20

# 1. class 선언
class Animal:
    name = "고양이"

    # sound라는 메서드
    def sound(self):
        print("야옹야옹")


# 2. class를 사용하기 위한 개체 생성
cat = Animal()

print(cat.name)
cat.sound()


# 클래스로 과일 이름/색상/맛 출력하기
# 들여쓰기 잘 보기
class Fruit:
    name = '사과'
    color = '빨간색'

    def taste(self):
        print('새콤하다')

    def vitamin(self):
        print('비타민 C가 풍부하다.')


apple = Fruit()
print('과일명 :%s' % apple.name)
print('색상   :%s' % apple.color)
apple.taste()
apple.vitamin()


class Student:
    name = '이순신'
    kor = 85
    eng = 100
    math = 95

    def getSum(self):
        sum = self.kor + self.eng + self.math
        return sum


lee = Student()
print('이름 : %s' % lee.name)
print('합계 : %d' % lee.getSum())
print('평균 : %.1f' % (lee.getSum()/3))


# 원지름 예제
class Circle:
    radius = 10

    def getArea(self):
        area = 3.141592 * self.radius * self.radius
        return area

    def getCircum(self):
        circum = 2 * 3.141592 * self.radius
        return circum


cir = Circle()
print('반지름: %d' % cir.radius)
print('원의 면적: %.2f' % cir.getArea())
print('원주의 길이: %.2f' % cir.getCircum())
