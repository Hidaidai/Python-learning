#!/usr/bin/python
# -*- coding: UTF-8 -*-

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]
print '====================='

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k
print '====================='

'''
这种执行for循环的遍历方式是通过索引
函数 len() 返回列表的长度，即元素的个数。 函数range()返回一个序列的数。
range(1,5)表示1,2,3,4;没有5
下面是有else的案例：
'''
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'
'''
else下的语句是在没有break的情况下才会执行，也就是循环正常执行完的情况下才执行
while else也是一样的
'''
