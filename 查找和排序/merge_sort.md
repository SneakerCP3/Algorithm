[点此返回首页](https://github.com/SneakerCP3/Algorithm)
### 归并排序

##### 1、归并排序基本思路：将多个有序的列表归并成一个大列表
##### 2、将需要排序的列表分解成很小的小列表，然后归并，利用递归思想

##### 3、跟其他排序不同的是，需要额外空间，排序元素要放在一个新的列表里面

```python
# 首先定义一个归并函数
def merge(li,low,mid,high):
    '''
    归并函数，将一个无序列表中的两个有序部分排序为一个有序列表
    :param li: 待排序的列表
    :param low: 列表最左侧
    :param mid: 两个无序列表的分隔点
    :param high: 列表最右侧
    :return: 排序完成的列表
    '''
    tmp = []                        # 临时列表，用于存放排序列表
    i = low                         # 左边列表的起始下标
    j = mid + 1                     # 右边列表的起始下标
    while i <= mid and j < high:
        if li[i] < li[j]:
            tmp.append(li[i])
            i += 1
        if li[i] > li[j]:
            tmp.append(li[j])
            j += 1

    # 如果两个列表长度不等，则循环执行完成后有一个列表里的元素需要移到临时列表中中
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j < high:
        tmp.append(li[j])
        j += 1

    li[low:high + 1] = tmp          # 将临时列表重新赋值给li，区间范围左开右闭
    return li

# 定义归并排序算法
def merge_sort(li,low,high):
    '''
    递归进行排序，调用merge方法
    :param li:
    :param low: 之所以要定义low和high，是为了递归的时候好处理
    :param high:
    :return:
    '''
    if low < high:  # 证明至少有2个元素
        mid = (low + high) // 2
        merge_sort(li,low,mid)
        merge_sort(li,mid + 1 ,high)
        merge(li,0,mid,len(li))
    return li

if __name__ == '__main__':
    li = [7,8,1,2,4,3,14,6]
    print(merge_sort(li,0,len(li)))
```

