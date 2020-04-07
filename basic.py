s = 'abcdef'
a=''
for x in range(0,len(s)):
    if x % 2 == 0 :
        a = a + s[x+1]
    else:
        a = a + s[x-1]
print(a)
