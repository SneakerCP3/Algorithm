### 快速排序思路

##### 1、取一个元素P（一般取第一个元素），使元素的位置调整到正确排序后所在的位置

##### 2、列表被p分成两部分，左边都比P小，右边都比p大

##### 3、递归完成排序：本质上是二叉树的中序遍历

首先定义一个partition函数,将列表分成2部分,并返回该值所在下标：

```
def partition(li,left,right):
    '''
    :param li: 待排序列表
    :param left: left和right分别为需要操作列表的范围
    :param right:
    :return: 返回第一个元素在排好序列表中的位置
    '''
    tmp = li[left]                                     # 将第一个元素取出来临时存放
    while left < right:                                # 循环条件，注意是 < ,不是 <=
    
    # 因为第一个元素在左边，所以先从右边开始查找，直到遇到比tmp小的数，停止循环，将此时的值放在左边空的位置
        while li[right] >= tmp and left < right:       # 注意循环条件有两个
            right -= 1
        li[left] = li[right]
        
     # 同理，在左边找比tmp大的数，放在右边空的位置
        while li[left] <= tmp and left < right:
            left += 1
        li[right] = li[left]

    li[left] = tmp                # 循环完成之后，剩下空位的地方就是tmp应该在的位置，将其归位
	return left
```

定义快速排序函数，调用partition：

```
def qucik_sort(li,left,right):
    '''
    :param li: 待排序列表
    :param left: left和right分别为需要操作列表的范围
    :param right:
    :return: 排序完成的列表
    '''
    if left < right:                                  # 至少有2个元素才可排序
        mid = partition(li,left,right)                # 中序遍历，先找到mid，然后递归调用
        qucik_sort(li,left,mid-1)
        qucik_sort(li,mid+1,right)
    return li

if __name__ == '__main__':
    li = [5,7,4,6,3,1,2,9]
    print(qucik_sort(li,0,len(li)-1))                 # right应为列表长度-1
```

