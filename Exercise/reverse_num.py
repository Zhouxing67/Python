"""
正整数的反转

Version: 0.1
Author: zhouxing
"""

num = int(input('num = '))
num_reverse = 0
while num > 0:
    num_reverse = num_reverse * 10 + num % 10
    num //= 10
print('num_reverse=%d' % num_reverse)
