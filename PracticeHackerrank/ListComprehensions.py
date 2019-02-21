x = y = z = 1
n = 2
#
# print [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
#
#Solve
# arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != n]
# #Output
# print(arr)
# print ([[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != n])



#Read input and append the list to main records list using List Compression
n = int(input())
# records = [[input(),float(input())] for i in range(int(input()))]
records = [[input(),float(input())] for i in range(n)]
print(records)

#sort the list using list compression set will avoid duplicates
mk_lst  = sorted(set(x[1] for x in records))

print(mk_lst)
print(records[0])

#loop through records and if marks matches with second highest sort and display the names
for name in sorted(x[0] for x in records if x[1] == mk_lst[1]):
        print(name)

