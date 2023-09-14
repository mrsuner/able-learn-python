# 奇偶数检查
# 检查一个数是否是偶数
# 计算 一个数 取余 2 是否为整数即可
def is_even(number):
    if number % 2 == 0:
        # return 用来表示一个参数的返回值，它可以是任意类型
        return True
    else:
        return False

# 我们会有另外一种写法，来约定函数的返回值类型和参数的类型
# def is_even(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     else:
#         return False


if __name__ == '__main__':
    number = input("请输入一个整数: ")
    number = int(number)
    if is_even(number):
        print(f"{number} 是偶数")
    else:
        print(f"{number} 是奇数")