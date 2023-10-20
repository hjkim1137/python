# __init__() 사용 예제
# 외부에서 가져오는 값 사용하기
# def "뛰고" __init__

# 클래스 멤버변수와 메소드
# 멤버변수(Member Variable) : 클래스 내부에서 사용되는 변수
# • 메소드(Method) : 클래스 내부에서 정의된 함수
# • 클래스를 사용하는 방식은 첫번째 매개변수에 self가 들어간다.
# • 클래스 안에__init__ 라는 초기화 메서드
# • 이 메서드는 클래스의 객체가 만들어질 때 자동으로 호출
# • 그 객체의 속성을 정해 준다.

class Member:
    # 초기화(self는 원래 있는 것)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showMember(self):
        print("이름 :%s" % self.name)
        print("나이 : %d" % self.age)


mem1 = Member("지민", 30)
mem1.showMember()

'''
이름 :지민
나이 : 30
'''
