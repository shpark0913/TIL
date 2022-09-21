def f(i, k, r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
                used[j] = 1         # a[j]가 사용됨으로 표시
                p[i] = a[j]         # p[i]는 a[j]로 결정
                f(i+1, k, r)           # p[i+1] 의 값을 결정하럭 이동
                used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 5
r = 5
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * r

# p[0] = 1     # 맨 앞은 1로 고정
# used[0] = 1
# f(1, N, r)
#
# p[0] = 2     # 맨 앞은 2로 고정
# used[1] = 1
# f(1, N, r)