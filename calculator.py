# Day01 项目：简单计算器

# 获取用户输入的两个数字
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

# 获取用户想进行的运算
operator = input("请输入运算符（+、-、*、/）：")

# 根据运算符进行计算
if operator == "+":
    result = num1 + num2
    print(f"计算结果：{num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"计算结果：{num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"计算结果：{num1} * {num2} = {result}")

elif operator == "/":
    if num2 == 0:
        print("错误：除数不能为 0")
    else:
        result = num1 / num2
        print(f"计算结果：{num1} / {num2} = {result}")

else:
    print("错误：不支持这个运算符")