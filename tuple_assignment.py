# a=open("file2.txt")
# b={}
# k=0
# for d in a:
#     print(d)
#     e=d.split()
#     print(e)
# for w in e:
#     b[w]=b.get(w,0)+1
# for a,b in b.items():
#     print(a,b)
#     if(b>k):
#         k=b
#         m=a
# print(m,k)

# f=open('file2.txt')
# c={}
# z=[]
# for i in f:
#     j=i.split()
#     print(j)
# for k in j:
#     c[k]=c.get(k,0)+1
# for x,y in c.items():
#     z.append(y,x))
# for h in z:
#     print(sorted())
# print(sorted(((y,x) for x,y in c.items()),reverse=True))

hand = open('file2.txt')
di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

tmp = list()
for k,v in di.items() :
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:5] :
    print(k,v)