# for in 说明：也是循环结构的一种，经常用于遍历字符串、列表，元组，字典等

strs = 'hello world'
for s in strs:
    print(s)

print('================')

# 遍历列表
l = ['鹅鹅鹅', '曲项向天歌', '锄禾日当午', '春种一粒粟']

for i in l:
    print(i)

# 可以获取下表，enumerate每次循环可以得到下表及元素
for i, v in enumerate(l):
    print(i, v)

print('================')

#遍历字典
d = {'a':'apple', 'b':'banana', 'c':'car', 'd': 'desk'}
for key in d:
    # 遍历字典时遍历的是键
    print(key, d.get(key))
print('================')
# for key, value in d.items():
# 上下两种方式等价 d.items() <=> dict.items(d)
for key, value in dict.items(d):
    print(key,"==", value)


# 可迭代对象：列表、元组、字典等都是可迭代对象，就是可以遍历的对象
#
# range，用法如下：
print('================')
print(range(10))
# 可以生成从0开始到10的连续整数的迭代对象
print(range(0, 10))
# 可以遍历
for i in enumerate(range(10)):
    print(i)
# 强制转换为列表
print(list(range(1, 11)))