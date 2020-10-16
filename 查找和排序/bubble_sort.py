# -*- coding: utf-8 -*-
# 排序算法：较差：冒泡、选择、插入     较好：快速、堆、归并

class Sort_algorithm:
    def bubble_sort(self,li):
        '''
        时间复杂度O(n^2)，不论元素是否已经有序，都会走完这n-1趟
        :param li:
        :return:
        '''
        n = len(li)
        for i in range(n - 1):                      # 表示需要交换n-1趟
            for j in range(n-i-1):                  # 0到n-i-1是尚未排序的范围，关键点,注意边界
                if li[j] > li[j+1]:
                    li[j], li[j+1] = li[j+1], li[j]
            # print(li)
        return li


    def bubble_sort_new(self,li):
        '''
        改进版的冒泡排序，增加判断，如果有一趟不发生交换，证明已经有序，则无需继续循环
        :param li:
        :return:
        '''
        n = len(li)
        for i in range(n - 1):
            exchange = False                      # 增加标识，默认为False
            for j in range(n - i - 1):
                if li[j] > li[j + 1]:
                    li[j], li[j + 1] = li[j + 1], li[j]
                    exchange = True               # 如果发生了交换，则标识变更为True
            if exchange == False:
                return li

        return li




if __name__ == '__main__':
    sort_algorithm = Sort_algorithm()
    li = [5,6,3,9,1,5,10,11,12]
    print(sort_algorithm.bubble_sort(li))

    print(sort_algorithm.bubble_sort_new(li))



