import re

n = int(input())

for i in range(n):
    phone = input()
    match = re.match(r"^[789]{1}[0-9]{9}$", phone)
    if match:
        print("YES")
    else:
        print("NO")