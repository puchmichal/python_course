import re


with open("test.txt") as f:
    file = f.readlines()

text = " ".join(file)
text = text.lower()

words = re.findall(r'\w+', text)

word_count = dict()

for word in words:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
