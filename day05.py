text = "hello python hello ai"
words = text.split()
print(words)

text = "Hello Python"
print(text.lower())

text = "   hello python   "
print(text.strip())

text = "hello, python!"
text = text.replace(",", "")
text = text.replace("!", "")

print(text)


words = ["python", "ai", "python", "git", "ai"]
unique_words = set(words)

print(unique_words)


words = ["python", "ai", "python","ai","ai"]

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


text = "python ai agent python"
words = text.split()
print(words)


words = ["python", "ai", "python", "git", "ai"]
unique_words = set(words)

print(unique_words)

# Day05 项目：词频统计程序

# 一段需要统计的文本
text = """
Python is good.
Python is useful.
AI agent uses Python.
I like Python and AI.
"""

# 1. 全部转成小写，避免 Python 和 python 被当成两个词
text = text.lower()

# 2. 去掉常见标点符号
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace("?", "")

# 3. 按空格拆分成单词列表
words = text.split()

# 4. 使用字典统计每个单词出现次数
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# 5. 输出统计结果
print("词频统计结果：")
for word, count in word_count.items():
    print(f"{word}: {count}")

# 6. 输出不重复单词数量
unique_words = set(words)
print(f"不重复单词数量：{len(unique_words)}")