s=input()
n=int(input())
s=list(s)
l=[]
op=""
for i in range(0,len(s),n):
    for j in range(i,i+n):
        op+=s[j]
    l.append(op)
    op=""

from collections import OrderedDict
for c in l:
    foo=c
    print ("".join(OrderedDict.fromkeys(foo)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
