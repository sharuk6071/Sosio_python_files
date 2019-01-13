# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

stdin = sys.stdin

s = stdin.readline().strip()
prev = ''
ct = 0
all = []
for c in s:
    if prev == c:
        ct += 1
    else:
        if ct > 0: all.append("({}, {})".format(ct, prev))
        ct = 1
        prev = c
if ct > 0: all.append("({}, {})".format(ct, prev))
print(' '.join(all))

