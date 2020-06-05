a=open("file2.txt")
b={}
k=0
for d in a:
    print(d)
    e=d.split()
    print(e)
for w in e:
    b[w]=b.get(w,0)+1
for a,b in b.items():
    print(a,b)
    if(b>k):
        k=b
        m=a
print(m,k)
#method 2

hand=open("file2.txt")
di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
         di[w] = di.get(w,0) + 1

largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest :
         largest = v
         theword = k


print('Done',theword,largest)


