'''
Question :
  다양한 수로 이루어진 배열에서, 주어진 수들을 M번 더하여 가장 큰 수를 구하여라!
  단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
  또한 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
N : 배열의 크기
M : 숫자가 더해지는 횟수
K : 최대 연속으로 더할 수 있는 횟수
'''

'''
Q) sort 함수와 sorted 함수의 차이는?

A) 
    sort는 리스트명.sort() 형식으로, 리스트의 원본값을 직접 수정.
    sorted는 sorted(리스트명) 형식으로, 리스트 원본값은 그대로이고 정렬 값을 반환.

'''

# 내 풀이

# N, M, K = map(int, input().split())
# nums = list(map(int, input().split()))
# nums.sort()
#
# max_1st = nums[-1]          # 배열에서 최댓값
# max_2nd = nums[-2]          # 배열에서 2번째 큰 값
#
# cnt = 0                     # 숫자들이 더해질 변수
#
# if M <= K:
#     print(max_1st * M)
# else:
#     if max_1st == max_2nd:
#         print(max_1st * M)
#     else:
#         print((M//(K+1)) * (K * max_1st + max_2nd) + (M % (K+1)) * max_1st)

################################################################################

# 책 풀이 1 - 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산을 반복하는, 단순한 풀이
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
#
# first = data[n-1]
# second = data[n-2]
#
# result = 0
#
# while 1:
#     for i in range(k):          # 가장 큰 수를 k번 더하기
#         if m == 0:              # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1                  # 더할 때마다 1씩 빼기
#     if m == 0:                  # m이 0이라면 반복문 탈출
#         break
#     result += second            # 두 번째로 큰 수를 한 번 더하기
#     m -= 1                      # 더할 때마다 1씩 빼기
#
# print(result)

# 로직 자체는 잘 짜여진 듯. m을 하나씩 빼 주는 방식이 너무 좋다.
# 하지만 M의 크기가 100억 이상이라면 시간 초과 판정을 받을 것.

################################################################################

# 책 풀이 2 - 반복되는 수열 이용
# 이 풀이는 내 풀이와 유사한 듯!!!

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n-1]
# second = data[n-2]
#
# # 가장 큰 수가 더해지는 횟수 계산
# count = int(m / (k+1)) * k
# count += m % (k+1)
#
# result = 0
# result += count * first         # 가장 큰 수 더하기
# result += (m - count) * second  # 두 번째로 큰 수 더하기


