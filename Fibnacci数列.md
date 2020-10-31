#### Fibnacci数列的三种实现方式：

这个数列从第3项开始，每一项都等于前两项之和。即0、1、1、2、3、5、8、13、21、34、……

1、递归：递归会有大量的重复计算，效率很低，不推荐

```python
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    return fibnacci(n-1)+fibnacci(n-2)
```

2、类似动态规划解法

```python
def fibnacci_no_recursion(n):
    f = [0,1,1]          # 额外的空间
    if n <= 2 and n>0:
        return 1
    if n >2:
        for i in range(n-2):  # 注意n-2
            num = f[-1] + f[-2]
            f.append(num)
    return f[-1]              # 结果就是列表最后一个数
```

3、类似动态规划解法-优化版

不需要那么大的额外空间，每次只需要存两个数字即可，故而可进行优化

```python
def fib_new(n):
    a = 1
    b = 1
    if n <= 2 and n>0:
        return 1
    for i in range(2, n + 1):
        a, b = b, a + b      # 关键代码
    return b      			
```

