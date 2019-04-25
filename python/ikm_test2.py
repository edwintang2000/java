#! /usr/bin/python3

import sys

def mycount(s, l):
    count = 0
    for i in range(0,len(l)-len(s)+1):
        if l[i:i+len(s)] == s:
            count = count+1
    return count
    
    
letters = ('A','G','C','T')
file = sys.stdin
for line in file:
    if str(line)[0] == '0':
        break
    sl = line.split()
    s = sl[0]
    l = sl[1]
    count1 = mycount(s,l)
    count2 = 0
    modified_set = {s[0:len(s)-1]}
    for i in range(0,len(s)):
        modified_set.add(s[0:i] + s[i+1:len(s)])
    for pattern in modified_set:
        count2 = count2 + mycount(pattern,l)
    
    count3 = 0
    modified_set = {'A'+s}
    for i in range(0,len(s)+1):
        for c in letters:
            modified_set.add(s[0:i] + c + s[i:len(s)])
    for pattern in modified_set:
        count3 = count3 + mycount(pattern,l)
    print(str(count1) + ' ' + str(count2) + ' ' + str(count3))
    