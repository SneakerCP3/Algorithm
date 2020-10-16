# -*- coding: utf-8 -*-
# 排序算法：较差：冒泡、选择、插入     较好：快速、拓扑、希尔

def select_sort(li):
    '''
    每次从列表中未完成排序区找出最小的一个数，放在无序区列表最左边，当循环完成之后，就完成排序
    :param li:
    :return:
    '''
    for i in range(len(li) - 1):                # 第i趟
        min_loc = i                             # 默认最小的数的下标是i，也就是最左边
        for j in range(i+1,len(li)):            # i之前的已经是排好序的，所以从i+1开始，也就是无序区
            if li[j] < li[min_loc]:
                min_loc = j                     # 找到了无序区里面最小的数的下标

        li[i],li[min_loc] = li[min_loc], li[i]  # 将最小的数与无序区里的最左边的数交换，注意要在第二个for循环外

    return li

if __name__ == '__main__':

    li = [5,9,3,4,6,8,1]
    print(select_sort(li))



