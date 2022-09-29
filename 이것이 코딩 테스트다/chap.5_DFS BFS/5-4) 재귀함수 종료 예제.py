def recursive_function():
    print('재귀함수를 호출합니다')
    recursive_function()

recursive_function()

def recursive_function(i):
    if i == 100:
        return
    print(f'{i}번째 함수에서 {i+1}번째 함수를 호출합니다.')
    recursive_function(i+1)
    print(f'{i}번째 함수를 종료합니다.')

recursive_function(1)