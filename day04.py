# 定义一个简单函数
def greet(name):
    print(f"你好，{name}欢迎学习 Python！")

# 调用函数
greet("嘉伟")

def add(a, b):
    return a + b

result = add(5, 3)
print("5 + 3 =", result)

def square(x):
    """
    计算数字的平方
    参数:
        x (int/float): 数字
    返回:
        int/float: x 的平方
    """
    return x ** 2

print(square(4))

from math import sqrt, ceil
print(sqrt(25))
print(ceil(4.2))

import mymath

print(mymath.add(10, 5))
print(mymath.subtract(10, 5))


def hello():
     print(f"你好，欢迎学习 Python！")


hello()
    