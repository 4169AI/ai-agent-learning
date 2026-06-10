# 根据你的 180 天学习表，Day03 可以开始接触：

# 列表（list）和字典（dict）
# 学习如何存储多个数据
# 列表的增删改查
# 字典的键值操作

# 这是你从基础语法过渡到数据结构的关键一天

# # 定义函数
# def greet(name):
#     print(f"你好，{name}！")

# # 调用函数
# greet("嘉伟")

# def add(a, b):
#     return a + b

# result = add(3, 5)
# print(result)  # 输出 8

# def greet(name="Python学习者"):
#     print(f"你好，{name}！")

# greet()        # 你好，Python学习者！
# greet("嘉伟")   # 你好，嘉伟！


# from text_tool import word_count
# text = "Python 是一个很好学的语言"
# print(word_count(text))  # 输出 7

# fruits = ["苹果", "香蕉", "橘子"]
# fruits.append("葡萄")  # 在末尾增加
# fruits.insert(1, "梨") # 插入到指定位置
# fruits.remove("香蕉")
# fruits.pop(0)  # 删除第一个元素
# print(fruits[0])  # 第一个元素
# print(fruits[-1]) # 最后一个元素
# for fruit in fruits:
#     print(fruit)
# print(fruits)

# person = {"name": "嘉伟", "age": 25, "goal": "AI Agent 开发工程师"}
# print(person["name"])
# person["city"] = "北京"
# person["age"] = 26
# print(person.get("age"))
# del person["goal"]
# for key, value in person.items():
#     print(key, value)

# fruits = ["苹果","香蕉","橘子"]
# fruits.append("葡萄")
# fruits.remove("香蕉")

# for fruits in fruits:
#     print(fruits)


# person = {"name":"嘉伟","age":"26","城市":"北京"}
# del person["城市"]
# person["邮箱"] = 1040167-0
# for key, value in person.items():
#     print(key, value) 

item = ["print", "input", "if else", "for", "while", "list", "dict"]
for item in item:
     print("我今天学习了：",item)