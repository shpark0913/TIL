arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1<<n):       # 공집합 빼고 싶으면 range(1, 1<<n)으로 하면 된다!
    for j in range(n):
        if i & (1<<j):      # j번 비트가 0이 아니면 arr[j] 부분집합의 원소
            print(arr[j], end = ' ')
    print()