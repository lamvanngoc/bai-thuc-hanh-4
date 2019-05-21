s=input('nhap cau:')
d={'h':0,'s':0}
for c in s:
    if c.isdigit():
        d['h']+=1
    elif c.isalpha():
        d['s']+=1
    else:
        pass
print('chu cai la:',d['h'])
print('chu so la:',d['s'])