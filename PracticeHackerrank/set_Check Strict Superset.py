A = input().split()
setA = set(A)
length_A = len(setA)

n = int(input())

check = True
# for i in range(n):
#     line = input().split()
#     setTemp = set(line)
#     if(setTemp not in setA or (setTemp in setA and length_A == len(setTemp))):
#         check = False

for i in range(n):
    line = input().split()
    setTemp = set(line)
    if(setA.issuperset(setTemp) == False):
        check = False

# print(setA)
print(check)


