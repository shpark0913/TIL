'''
그래프 순회 :
    비선형구조인 그래프로 표현된 모든 자료(정점)를
    빠짐없이 탐색하는 것을 의미한다.
  ex) DFS(깊이우선탐색), BFS(넓이우선탐색)

  - 선형구조 : 자료 간의 관계가 1대1의 관계를 갖는다.
  - 비선형구조 : 자료 간의 관계가 1대N의 관계를 갖는다. (ex: 트리)
'''

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
print(queue)
