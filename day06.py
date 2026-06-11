
# 完成今天的学习后，你应该能：

# 读取和写入文本文件（txt）
# 处理文件路径和打开模式（r/w/a）
# 了解常见异常（如文件不存在、除零错误）
# 使用 try…except 捕获异常
# 完成一个小项目：读取文件并统计行数、单词数
# 提交今日交付物到 GitHub


# Day06.py
# 主题：文件操作与异常处理

# ---------------------------
# 练习 1：读取文件
try:
    with open("example.txt", "r") as f:
        print("练习 1：读取文件内容")
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("错误：example.txt 文件不存在，请先创建文件")

print("---------------------------")

# ---------------------------
# 练习 2：写入文件
try:
    with open("output.txt", "w") as f:
        f.write("Hello Python!\n")
        f.write("今天学习文件操作与异常处理\n")
    print("练习 2：文件写入完成")
except Exception as e:
    print("写入文件时出错：", e)

# 读取刚写入的文件
try:
    with open("output.txt", "r") as f:
        print("文件内容预览：")
        print(f.read())
except FileNotFoundError:
    print("错误：output.txt 文件不存在")

print("---------------------------")

# ---------------------------
# 练习 3：异常处理
try:
    num = int(input("请输入一个数字："))
    print("10 除以你输入的数字 =", 10 / num)
except ZeroDivisionError:
    print("错误：不能除以 0")
except ValueError:
    print("错误：请输入有效的数字")

print("---------------------------")

# ---------------------------
# 练习 4：统计文件行数和单词数
try:
    with open("example.txt", "r") as f:
        lines = f.readlines()
    line_count = len(lines)
    word_count = 0
    for line in lines:
        word_count += len(line.split())
    print(f"练习 4：文件统计结果 -> 总行数: {line_count}, 总单词数: {word_count}")
except FileNotFoundError:
    print("错误：example.txt 文件不存在，无法统计")