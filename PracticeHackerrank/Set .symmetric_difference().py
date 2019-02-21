n1 = int(input())
s1 = input().split()
setS1 = set(s1)

n2 = int(input())
s2 = input().split()
setS2 = set(s2)

symmetric_difference = setS1.symmetric_difference(setS2)
print(len(symmetric_difference))
