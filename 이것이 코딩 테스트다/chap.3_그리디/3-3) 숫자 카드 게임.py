'''
숫자 카드 게임

Question)
    1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있따. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
    2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
    3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
    4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려해
      최종적으로 가장 높은 숫자를 뽑을 수 있도록 전략을 세워야 한다.
'''
'''
예제1) 답 : 2
3 3
3 1 2
4 1 4
2 2 2

예제2) 답 : 3
2 4
7 3 1 8
3 3 3 4
'''

#########################################################################

# 내 풀이

# N, M = map(int, input().split())
# cards = [list(map(int, input().split())) for _ in range(N)]
# value = min(cards[0])
#
# for i in range(1, len(cards)):
#     min_num = min(cards[i])
#     if min_num > value:
#         value = min_num
#
# print(value)

#########################################################################

# 책 풀이 1 - min() 함수를 이용
# N, M = map(int, input().split())
#
# res = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     res = max(res, min_value)
# print(res)

# 내 풀이와 유사. 난 반복문을 사용했지만 교재에서는 max 함수를 사용함.

#########################################################################

# 책 풀이 2 - 2중 반복문 구조를 이용

# N, M = map(int, input().split())
#
# res = 0
# for i in range(N):
#     data = list(map(int, input().split()))
#     min_value = 10001           # 가장 작은 수 찾기 위한 변수
#     for a in data:
#         min_value = min(min_value, a)
#     res = max(res, min_value)
#
# print(res)

#########################################################################
