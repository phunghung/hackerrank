n = int(input())
integer_list = map(int, input().split())

tup = tuple(integer_list)

print(tup)
print(type(tup))
print(hash(tup))