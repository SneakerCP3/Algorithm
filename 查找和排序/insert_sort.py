# -*- coding: utf-8 -*-
def insert_sort(li):
    '''
    想象插入扑克牌的场景
    :param li:
    :return:
    '''
    for i in range(1,len(li)):          # i表示摸到的牌的下标,刚开始的手牌是第一个数，所以摸牌从第二个数开始
        tmp = li[i]
        j = i - 1                       # j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)

    return li

if __name__ == '__main__':

    li = [5,9,3,4,6,8,1]
    print(insert_sort(li))


