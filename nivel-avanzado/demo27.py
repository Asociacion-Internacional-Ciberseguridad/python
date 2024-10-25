from collections import deque

cola = deque([1, 2, 3])
cola.append(4)
cola.appendleft(0)
print(cola)
cola.pop()
cola.popleft()
print(cola)
