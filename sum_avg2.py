#list
s=list()
while True:
    a=input("enter the nos")
    if a=='done':
        break
    b=float(a)
    s.append(b)
avg=sum(s)/len(s)
print(avg)