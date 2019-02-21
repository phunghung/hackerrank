n1 = int(input())
s1 = input().split()
setS1 = set(s1)

n2 = int(input())
s2 = input().split()
setS2 = set(s2)

print(setS1)
print(type(setS1))

print(setS2)
print(type(setS2))

intersection = setS1.intersection(setS2)
print(len(intersection))