def f(i, k, s, t):
    global answer
    if i == k:                  # 모든 원소가 고려된 경우
        if s == t:              # 부분집합의 합이 t면
            answer += 1
        return
    else:
        f(i+1, k, s + a[i], t)  # a[i]가 포함된 경우
        f(i+1, k, s, t)         # a[i]가 포함되지 않은 경우

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answer = 0
f(0, 10, 0, 10)
print(answer)

######################################################

# 가지치기한 경우 ( s가 t를 넘으면 가지치기)
def f(i, k, s, t):
    global answer
    if i == k:                  # 모든 원소가 고려된 경우
        if s == t:              # 부분집합의 합이 t면
            answer += 1
        return
    elif s > t:
        return
    else:
        f(i+1, k, s + a[i], t)  # a[i]가 포함된 경우
        f(i+1, k, s, t)         # a[i]가 포함되지 않은 경우

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answer = 0
f(0, 10, 0, 10)
print(answer)

######################################################


