# 재귀 호출을 통한 순열 생성

# p : 원소가 저장된 배열
# k : 원소의 개수, i : 선택된 원소의 인덱스

def f(i, k):
    if i == k:                          # 인덱스 i == 원소의 개수
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i + 1, k)
            p[i], p[j] = p[j], p[i]     # 원상복구

p = [1, 2, 3]
f(0, 3)  # 0번 원소부터 시작, 원소는 3개
