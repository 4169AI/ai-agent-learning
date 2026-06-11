# 理解什么是 类 class
# 理解什么是 对象 object
# 会使用 __init__() 初始化对象
# 会给对象添加属性
# 会定义对象方法
# 理解简单继承
# 完成 bank_account.py 银行账户管理程序


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"大家好，我叫{self.name}，今年{self.age}岁")

# student1 = Student("嘉伟", 25)
# student1.introduce()

# Day07 项目：银行账户管理

# class BankAccount:
#     def __init__(self, owner, balance):
#         # 账户主人
#         self.owner = owner

#         # 账户余额
#         self.balance = balance

#     def show_balance(self):
#         # 显示余额
#         print(f"{self.owner} 的账户余额是：{self.balance} 元")

#     def deposit(self, amount):
#         # 存钱
#         self.balance += amount
#         print(f"成功存入 {amount} 元")
#         self.show_balance()

#     def withdraw(self, amount):
#         # 取钱
#         if amount > self.balance:
#             print("余额不足，取款失败")
#         else:
#             self.balance -= amount
#             print(f"成功取出 {amount} 元")
#             self.show_balance()


# # 创建一个银行账户对象
# account1 = BankAccount("嘉伟", 1000)

# # 查看余额
# account1.show_balance()

# # 存钱
# account1.deposit(500)

# # 取钱
# account1.withdraw(300)

# # 尝试取超过余额的钱
# account1.withdraw(2000)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age

#     def introduce(self):
#         print(f"大家好，我叫{self.name}，今年{self.age}岁")

# Student1 = Student("张三", 20)
# Student1.introduce()

# class Car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def show_info(self):
#          print(f"这是一辆{self.brand}汽车，价格是{self.price}元")

# car1 = Car("长安深蓝", 15)   
# car1.show_info() 

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} 的账户余额是：{self.balance} 元")


class CreditAccount(BankAccount):
    def __init__(self, owner, balance, credit_limit):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def show_credit_limit(self):
        print(f"{self.owner} 的信用额度是：{self.credit_limit} 元")


credit1 = CreditAccount("嘉伟", 1000, 5000)
credit1.show_balance()
credit1.show_credit_limit()