def SelectionSort(A):                   # 선택 정렬
    n = len(A)
    for i in range(n-1):
        minI = i                        # idx i를 minIdx라고 가정
        for j in range(i+1, n):
            if A[minI] > A[j]:          # idx j < minIdx이면 min 수정
                minI = j
        A[i], A[minI] = A[minI], A[i]   # 순회 마친 후 최소 원소를 idx i에 할당
    return A

print(SelectionSort([1, 3, 4, 2]))      # [1, 2, 3, 4] 가 답이다.