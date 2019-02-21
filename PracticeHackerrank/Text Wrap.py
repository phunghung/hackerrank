# s = input()
# w =  int(input())
#
# for i in range(0,len(s),w):
#     print(s[i:i+w])

import string

s = input()

print(s.capitalize().title())
print(' '.join(i.capitalize() for i in s.split(' ')))
