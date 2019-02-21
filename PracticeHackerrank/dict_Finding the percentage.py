n = int(input())
student_mark = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_mark[name] = scores

query_name = input()

# average_mark = 0
total_mark = 0

lst_score = student_mark[query_name]
print(lst_score)

for i in range(len(lst_score)):
    total_mark += lst_score[i]


print("%.2f" %(total_mark/len(lst_score)))
