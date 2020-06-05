#assigning the tuples
(x,y,z)=(2,3,4)
print(x)
print(y)
print(z)

#tuples and dictionaries
d={1:2,3:4}
k=d.items()
print(k)

#tuples are cpmparable
b=((0,1,2)<(5,1,2))
print(b)
e=((0,1,20000)<(0,3,4))
print(e)
r=(("jones","sally")<("jones",'sam'))
print(r)
t=(("jones","sally")>('adams','sam'))
print(t)