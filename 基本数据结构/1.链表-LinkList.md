### 链表

链表是一种在存储单元上非连续、非顺序的存储结构。数据元素的逻辑顺序是通过链表中的指针链接次序实现。链表是由一系列的结点组成，结点可以在运行时动态生成。每个结点包含两部分：数据域与指针域。数据域存储数据元素，指针域存储下一结点的指针。

单链表（即单向链表）的Python实现：

#### 先定义节点类：

```python
class Node(item):
    # item存放数据元素
    self.item = item
    # next是下一个节点的标识
    self.next = None
```

#### 定义单链表及方法：

```python
class SingleLinkList():
    '''为链表定义一些方法'''
    def __init__(self):
        '''单链表，链表需要具有首地址指针head'''
        self.head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.head is None

    def length(self):
        '''链表长度'''
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            # 指针下移
            cur = cur.next
        return count

    def itmes(self):
        '''获取链表数据迭代器，遍历链表'''
        cur = self.head
        while cur is not None:
            # 返回生成器
            yield cur.item
            # 指针下移
            cur = cur.next
            
    def add(self,item):
        '''向链表头部添加元素，头插法'''
        node = Node(item)
        # 新节点指针指向原头部节点
        node.next = self.head
        # 头部节点指针修改为新节点
        self.head = node

    def append(self,item):
        '''尾部添加元素，尾插法'''
        node = Node(item)
        # 先判断是否为空链表
        if self.is_empty():
            # 空链表，head指向新节点
            self.head = node
        else:
            # 不是空链表，则找到尾邻，将尾部next节点指向新节点
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            
    def insert(self,index,item):
        '''指定位置插入元素'''
        # 指定位置在第一个元素之前，在头部插入
        if index <= 0:
            self.add(item)
        # 指定位置超过尾部，在尾部插入
        elif index >= (self.length() - 1):
            self.append(item)
        else:
            # 创建元素节点
            node = Node(item)
            cur = self.head
            for i in range(index - 1 ):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        ''' 删除节点 '''
        cur = self.head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def find(self,item):
        '''
        查找元素是否存在
        :param item:
        :return:
        '''
        return item in self.itmes()
```

#### 链表类的解题套路：

1、随机取一个node（例如：Node(-1）)定义一个假头，指向self.head，题目最后返回 node.next

2、链表的题一般需要画出链表图示，以便于理解
