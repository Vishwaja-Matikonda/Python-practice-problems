#sort by value
#using for loop
d={'a':1,'c':2,'b':3}
l=[]
for i,j in d.items():
    l.append((j,i))
print(l)

#shortcut method
d={'a':1,'c':2,'b':3}
print(sorted((j,i) for i,j in d.items()))
