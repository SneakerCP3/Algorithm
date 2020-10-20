#### 队列-Queue

1、队列（Queue）是一个数据集合，仅允许在列表的一端进行插入，另一端进行删除。

2、进行插入的一端成为队尾（rear），插入动作成为进队或者入队

3、进行删除的一端称为队头（front），删除动作成为出队

4、队列的性质：先进先出（First in，First out）

##### Python实现队列（环形队列）：

```python
class Queue:
    def __init__(self,size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0   # 队尾指针
        self.front = 0  # 队头指针

    def push(self,element):
        if not self.is_filled():            #插入的时候判断是否队满
            rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('Queue is filled.')

    def pop(self):
        if not self.is_empty():              #pop的时候判断是否队空
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError('Queue is empty.')

    # 判断队空
    def is_empty(self):
        return self.rear == self.front

    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front
```

##### Python内置的队列模块（不要反复造轮子，实际中直接用现成的队列结构）

```python
# Python内置的队列，支持双向队列
# 导入方法
from collections import deque

# 单向队列：常用
q = deque()   # 创建queue，可指定大小
q.append(1)   # 队尾进队
q.popleft()   # 队首出队

# 双向队列：不常用
q.appendleft() # 队首进队
q.pop()        # 队尾出队

```

