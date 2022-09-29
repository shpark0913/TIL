# 선택정렬

# def SelectionSort(A):
#     n = len(A)
#     for i in range(n-1):
#         minI = i
#         for j in range(i, n):
#             if A[j] < A[minI]:
#                 minI = j
#         A[minI], A[i] = A[i], A[minI]

########################################################

# 팩토리얼

# 재귀
# def fac(n):
#     if n <= 1:
#         return 1
#     else:
#         return n*fac(n-1)
#
# print(fac(5))   # 120

########################################################

# 2^k 연산에 대한 재귀와 반복

# 재귀

# def power_2(n):
#     if n == 0:
#         return 1
#     else:
#         return 2*power_2(n-1)

# 반복

# def power_2(n):
#     a = 1
#     for i in range(n):
#         a *= 2
#     return a
#
# print(power_2(5))

########################################################

# 단순하게 수열을 생성하는 방법
# {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수

# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i1 != i2:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)

########################################################

# 재귀 호출을 통한 순열 생성
# p : 데이터가 저장된 배열
# k : 원소의 개수, i : 선택된 원소의 수

# def f(i, k):
#     if i == k:
#         print(p)
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]


########################################################

# used 배열 이용
# n! 의 경우를 따져보겠다.
# p : 순열을 저장하는 배열
# a : 순열을 만드는데 사용할 숫자 배열
# k : 원소의 개수, i : 선택된 원소의 개수
# used[K-1] : 사용 여부, p : 결과 저장 배열

# def f(i, k):
#     if i == k:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:
#                 used[j] = 1
#                 p[i] = a[j]
#                 f(i+1, k)
#                 used[j] = 0
#
# N = 3
# a = [i for i in range(1, N+1)]
# p = [0] * N
# used = [0] * N
#
# f(0, N)

########################################################

# 위의 경우랑 유사하지만, 위의 경우는 n!을 나타낸 것이고
# 지금은 nPr을 나타내는 것이다. ex) 10P3

# def f(i, k, r):
#     if i == r:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:
#                 used[j] = 1
#                 p[i] = a[j]
#                 f(i+1, k, r)
#                 used[j] = 0
#
# N = 10
# r = 3
# a = [i for i in range(1, N+1)]
# p = [0] * r
# used = [0] * N
#
# f(0, N, r)

########################################################

# 단순하게 모든 부분 집합 생성하는 방법
# 4개 원소를 포함한 집합에 대한 Power Set 구하기

# for i1 in range(2):
#     bit = [0] * 4
#     bit[0] = i1
#     for i2 in range(2):
#         bit[1] = i2
#         for i3 in range(2):
#             bit[2] = i3
#             for i4 in range(2):
#                 bit[3] = i4
#                 print(bit)

########################################################

# 바이너리 카운팅을 통한 사전적 순서
# 부분집합을 생성하기 위한 가장 자연스러운 방법이다.
# 바이너리 카운팅은 사전적 순서로 생성하기 위한 가장 간단한 방법이다.

# 원소 수에 해당하는 N개의 비트열을 이용한다.
# n번째 비트값이 1이면 n번째 원소가 포함되었음을 의미한다.

# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i&(1<<j):
#             print(arr[j], end = ' ')
#     print()

########################################################

# 부분집합 재귀로 표현하기

# def f(i, k):
#     if i == k:
#         # print(bit)            # 비트 구경하기
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j], end = ' ')
#         print()
#     else:
#         bit[i] = 0
#         f(i+1, k)
#         bit[i] = 1
#         f(i+1, k)
#
# arr = [3, 6, 7]
# n = len(arr)
# bit = [0] * n            # bit[i] : arr[i]가 부분집합의 원소인지 표시
# f(0, n)

########################################################

# 10개 중에서 3개를 조합으로 뽑는 경우

# N = 10
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             print(i, j, k)

########################################################

# 조합. n개에서 r개를 고르기. s : 선택할 수 있는 구간의 시작
# def nCr(n, r, s):       # n개에서 r개를 고르는 조합, s 선택할 수 있는 구간의 시작
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = A[i]
#             nCr(n, r-1, i+1)
#
# A = [1, 2, 3, 4, 5]
# n = len(A)
# r = 3
# comb = [0] * r
# nCr(n, r, 0)








