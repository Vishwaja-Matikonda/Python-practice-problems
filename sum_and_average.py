#sum and average of given numbers
#without list
c=0
d=0
while True:
    a=input("enter the nos")
    if a=='done':
        break
    b=float(a)
    c=c+b
    d=d+1
avg=c/d
print(avg)
