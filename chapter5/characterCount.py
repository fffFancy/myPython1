import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    # 用来确保键存在于字典
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# print(count)
# pprint.pprint(count)
print(pprint.pformat(count))