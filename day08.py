# day08.py
# Day08：函数与面向对象综合练习
# 主题：增强版银行账户 + 文件保存 + 类方法 + 转账函数


class BankAccount:
    # 类属性：所有账户共用的利率
    interest_rate = 0.03

    def __init__(self, owner, balance):
        # 账户主人
        self.owner = owner

        # 账户余额
        self.balance = balance

    def show_balance(self):
        # 显示账户余额
        print(f"{self.owner} 的账户余额是：{self.balance} 元")

    def deposit(self, amount):
        # 存钱
        if amount <= 0:
            print("存款金额必须大于 0")
            return

        self.balance += amount
        print(f"{self.owner} 成功存入 {amount} 元")
        self.show_balance()

    def withdraw(self, amount):
        # 取钱
        if amount <= 0:
            print("取款金额必须大于 0")
            return

        if amount > self.balance:
            print(f"{self.owner} 余额不足，取款失败")
        else:
            self.balance -= amount
            print(f"{self.owner} 成功取出 {amount} 元")
            self.show_balance()

    def save_to_file(self):
        # 把账户信息保存到 txt 文件
        file_name = f"{self.owner}_account.txt"

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"账户主人：{self.owner}\n")
            f.write(f"账户余额：{self.balance}\n")
            f.write(f"当前利率：{BankAccount.interest_rate}\n")

        print(f"{self.owner} 的账户信息已经保存到 {file_name}")

    def read_from_file(self):
        # 从 txt 文件读取账户信息
        file_name = f"{self.owner}_account.txt"

        try:
            with open(file_name, "r", encoding="utf-8") as f:
                content = f.read()

            print(f"{self.owner} 的账户文件内容：")
            print(content)

        except FileNotFoundError:
            print(f"错误：找不到 {file_name} 文件，请先保存账户信息")

    @classmethod
    def show_rate(cls):
        # 类方法：显示所有账户共用的利率
        print(f"当前银行利率是：{cls.interest_rate}")


def transfer(from_account, to_account, amount):
    # 从一个账户转账到另一个账户
    if amount <= 0:
        print("转账金额必须大于 0")
        return

    if amount > from_account.balance:
        print("余额不足，转账失败")
    else:
        from_account.balance -= amount
        to_account.balance += amount

        print(f"转账成功：从 {from_account.owner} 转账 {amount} 元给 {to_account.owner}")
        from_account.show_balance()
        to_account.show_balance()


# 主程序入口
if __name__ == "__main__":
    print("Day08：函数与面向对象综合练习")
    print("---------------------------")

    # 显示银行利率
    BankAccount.show_rate()

    print("---------------------------")

    # 创建两个银行账户对象
    account1 = BankAccount("嘉伟", 1000)
    account2 = BankAccount("小明", 500)

    # 显示初始余额
    account1.show_balance()
    account2.show_balance()

    print("---------------------------")

    # 存钱和取钱
    account1.deposit(300)
    account2.withdraw(100)

    print("---------------------------")

    # 转账
    transfer(account1, account2, 500)

    print("---------------------------")

    # 保存账户信息到文件
    account1.save_to_file()
    account2.save_to_file()

    print("---------------------------")

    # 从文件读取账户信息
    account1.read_from_file()
    account2.read_from_file()