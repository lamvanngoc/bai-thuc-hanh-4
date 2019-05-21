a=input('nhap cau: ')
dict={"h":0,"t":0}
for c in a:
    if c.isupper():
        dict["h"]+=1
    else:
        if c!=" ":
           dict["t"]+=1
print(dict)
print(dict)