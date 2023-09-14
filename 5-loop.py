import pprint

# 使用for循环打印前5个整数
print("使用for循环打印前5个整数:")

for i in range(1, 6):
    print(i)

# range函数用于生成一个整数序列，语法为range(start, stop[, step])，其中start为起始值，stop为结束值，step为步长，默认为1。
# range(1, 6)生成的整数序列为[1, 2, 3, 4, 5]，不包含6。

# 所以上面的方法也可以写成：
print("\n使用for循环打印前5个整数:")
for i in [1, 2, 3, 4, 5]:
    print(i)

# 使用while循环打印前5个整数
print("\n使用while循环打印前5个整数:")
count = 1
while count <= 5:
    print(count)
    count += 1
