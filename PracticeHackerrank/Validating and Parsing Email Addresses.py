import re

n = int(input())

pattern = r"^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$"
for i in range(n):
    name, addr = input().split(' ')
    match = re.match(pattern, addr)
    if match:
        print(name, addr)