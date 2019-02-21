s = input()
lst = list(s)

index, character = input().split(" ")


lst[int(index)] = character
s = ''.join(lst)
print(s)

def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string = ''.join(lst)
    return string