N = int(input())        # 모험가 수

adventurer = list(map(int, input().split()))
adventurer.sort()

num_people = 0
num_group = 0
for person in adventurer:
    num_people += 1
    if num_people > person:
        num_group += 1
        num_people = 0

print(num_group)