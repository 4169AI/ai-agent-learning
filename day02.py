score = 85

# if score>= 90:
#     print("优秀")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")

for i in range(5):
    print("循环次数:",i)

i = 0
while i < 5:
    print("当前 i =", i)
    i += 1

total = 0
for i in range(1, 101):
    total += i
print("1 到 100 的和是：", total)


secret = 7
guess = None

# while guess != secret:
#     guess = int(input("猜一个 1~10 的数字："))
#     if guess < secret:
#         print("太小了")
#     elif guess > secret:
#         print("太大了")
#     else:
#         print("恭喜你，猜对了！")

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end="\t")
    print()


# 下列条件语句输出结果是什么？
# score = 75
# if score > 80:
#     print("优秀")
# elif score > 60:
#     print("及格")
# else:
#      print("不及格")
# for i in range(1, 6): print(i) 输出什么？
# for i in range(1, 6): print(i)
# 用 while 写一个循环，让 n 从 1 加到 10 并输出总和。
# Total = 0
# n = 1
# while n<11:
#     Total = Total+n
#     n+=1
#     print("1加到10",Total)

# 写一个程序，输入一个整数，判断它是否是偶数。
# M = int(input("请输入一个数字:"))
# if M % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")

# 写一个程序，用循环打印从 1 到用户输入的数字，每行打印该数字个 *。
# 让用户输入一个数字
num = int(input("请输入一个数字："))

# 从 1 循环到 num
for i in range(1, num + 1):
    # 每一行打印 i 个星号
    print("*" * i)