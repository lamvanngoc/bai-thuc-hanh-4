import sys
a=0
while True:
    s=input('nhap nhat ky:')
    if not s:
        break
    b=s.split(' ')
    c=b[0]
    y=int(b[1])
    if c=='D':
        a+=y
    elif c=='W':
        a-=y
    else:
        pass
print(a)