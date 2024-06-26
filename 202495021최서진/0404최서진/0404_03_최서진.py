'''
    작성일 : 2024년 3월 21일
    작성자 : 컴퓨터 공학부, 202495021, 최서진
    설명 : 숫자와 연산자를 입력 받아 사칙연산의 결과 출력

    [문제분석]
        필요한 변수 : num1 num2 op 
        사칙연산 : + - * /
        두 개의 정수와 연산자를 입력 받는다.
        
        사칙연산을 제외한 모든 문자는 잘못된 입력이다. 나머지처리한다(else)
    [알고리즘]
        1. 숫자 두개를 입력 받는다.
            1-1첫번째 숫자를 입력받는다
            1-2연산자를 입력받는다
            1-3두번째 순자를 입력받는다.
            1-4연산자를 입력받는다
        2. 사칙연산 을 입력받는다.
            2-1. 사칙연산은 위 4개의 문자를 제외한 나머지는 else 처리한다
        3. 결과를 출력한다.
'''

num1 = int(input("num1을 입력하시오. : "))
num2 = int(input("num2를 입력하시오. : "))
op = int(input("사칙 연산을 입력하시오 : "))
if op == '+' : 
    print(f"{num1}+{num2}입니다.")
if op == '-' : 
    print(f"{num1}-{num2}입니다.")
if op == '*' : 
    print(f"{num1}*{num2}입니다.")
if op == '/' : 
    print(f"{num1}/{num2}입니다.")

