# used라는 배열 이용
# n! 의 경우를 따지는 것이다
# nPr 의 경우는 permutaion4에 구현을 해 두겠다.

def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
                used[j] = 1         # a[j]가 사용됨으로 표시
                p[i] = a[j]         # p[i]는 a[j]로 결정
                f(i+1, k)           # p[i+1] 의 값을 결정하럭 이동
                used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 3
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * N
f(0, N)