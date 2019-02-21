# def execute(lst, cmd, *args):
#     if cmd == 'insert':
#         lst.insert(int(args[0]), int(args[1]))
#     elif cmd == 'print':
#         print(lst)
#     elif cmd == 'remove':
#         lst.remove(int(args[0]))
#     elif cmd == 'append':
#         lst.append(int(args[0]))
#     elif cmd == 'sort':
#         lst.sort()
#     elif cmd == 'reverse':
#         lst.reverse()
#     elif cmd == 'pop':
#         lst.pop()
#     else:
#         print("Command not recognized!")
#
# lst = []
# for _ in range(int(input())):
#     execute(lst, *input().split())

lst = []

N = int(input())

for i in range(0, N):
    cmd = input().split()

    if cmd[0] == 'insert':
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print (lst)
    elif cmd[0] == 'remove':
        lst.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        lst.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        lst.sort()
    elif cmd[0] == 'pop':
        lst.pop()
    elif cmd[0] == 'reverse':
        lst.reverse()

