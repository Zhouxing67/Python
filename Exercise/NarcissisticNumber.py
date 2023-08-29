"""
找出所有水仙花数

Version: 0.1
Author: zhouxing
"""

for i in range(100, 1000):
    j = i % 10
    k = (i // 10) % 10
    n = (i // 100) % 10
    if i == j ** 3 + k ** 3 + n ** 3:
        print('i=%d' % i)
