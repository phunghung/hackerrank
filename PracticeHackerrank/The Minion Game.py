s = input()

vowels = 'AEIOU'

STUART_Score = 0
KEVIN_Score = 0
for i in range(len(s)):
    if s[i] in vowels:
        KEVIN_Score += (len(s)-i)
        print(i, ": ", s[i])
    else:
        STUART_Score += (len(s)-i)
        print(i, ": ", s[i])

if(STUART_Score > KEVIN_Score):
    print("Stuart", STUART_Score)
elif (STUART_Score < KEVIN_Score):
    print("Kevin", KEVIN_Score)
else:
    print("Draw")