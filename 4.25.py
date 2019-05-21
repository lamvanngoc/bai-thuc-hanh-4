a=input('nhap day so:')
b=[x for x in a.split(",") if int(x)%2!=0]
print(','.join(b))