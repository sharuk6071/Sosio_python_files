word = input()
n = len(word)
s, k = 0, 0
subs = set()
vowels = ('A', 'E', 'I', 'O', 'U')
for start in range(n):
    if word[start] in vowels:
        k += n - start
    else:
        s += n - start
if k > s:
    print("Kevin " + str(k))
elif s > k:
    print("Stuart " + str(s))
else:
    print("Draw")
