# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 2
# 입력 : n
# 출력 : 1부터 n까지의 숫자를 더한 값
"""
n(n+1)/2

1. 위 공식을 참고하여 변수 n을 입력받아 1부터 n까지 연속한 숫자의 합을 반환하는 함수 sum_n을 작성하세요.

2. 함수 sum_n에 10을 넣어 출력하세요.

3. 함수 sum_n에 100을 넣어 출력하세요.
"""
# 1번을 해보세요!
def sum_n(n):
	a = n * (n+1) / 2
	print(int(a))
# 2번을 해보세요!
print(sum_n(10))
# 3번을 해보세요!
print(sum_n(100))
