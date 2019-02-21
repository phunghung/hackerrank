# a = int(input())
# b = int(input())

# N = int(input())
# for i in range(0,N):
#     print(i**2)

# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if(year % 4 == 0 and year % 100 != 0):
#         leap = True
#     elif(year % 400 == 0):
#         leap = True
#     return leap
#
# year = int(input())
# print(is_leap(year))

# N = int(input())
# for i in range(1,N+1):
#     print(i,end='')

# s = input()
# # print(s.swapcase())
# print('-'.join(s.split(' ')), end='')

# a = input()
# b = input()
# print("Hello ", a, " ", b,"! You just delved into python.", sep='')

# lst = [2, 3, 6, 6, 5]
# n = int(input())
# arr = map(int, input().split())
# lst = list(arr)
# s = set(lst)
# s.remove(max(s))
# print(max(s))


# print(max(lst))
# lst.remove(max(lst))
# print(max(lst))
# lst.remove(max(lst))
# print(max(lst))

# s = set(lst)
# print(s)
# print(max(s))
# s.remove(max(s))
# print(s)


n = int(input())
student_mark = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_mark[name] = scores
    print(student_mark)

# query_name = input()