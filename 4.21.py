value=[]
items=[x for x in input('nhap chuoi nhi phan:').split(',')]
for p in items:
    intp=int(p,2)
    if not intp%5:
        value.append(p)
print(','.join(value))