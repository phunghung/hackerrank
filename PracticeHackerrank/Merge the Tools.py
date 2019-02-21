from re import *

# print(sub("e|l", "", "Hello People"))

s = input()
k = int(input())

setTemp = set()
lst = list()

for i in range(0, len(s), 3):
    # it = 0
    j = i+3
    if(j > len(s)):
        break;
    setTemp = s[i:i+3]
    # print(setTemp)
    lst = list(setTemp)
    if(lst[2] in lst[1]):
        lst.remove(lst[2])
    elif(lst[2] in lst[0]):
        lst.remove(lst[2])
    elif (lst[1] == lst[0]):
        lst.remove(lst[1])
    print(lst[0],lst[1],sep="")
    # for el in setTemp:
    #     if el not in lst:
    #         lst.append(el)
    # print(lst)

    # print("".join(set(setTemp)))

for part in zip(*[iter(s)] * k):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

s = input()
k = int(input())
num_subsegments = int(len(s) / k)

# -------------------------------------------- Editorial -----------------------------------
for index in range(num_subsegments):
    # Subsegment string
    t = s[index * k: (index + 1) * k]

    # Subsequence string having distinct characters
    u = ""

    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
            u += c

    # Print final converted string
    print(u)