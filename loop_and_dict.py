#retrieving both keys and values
#method 1
c={1:2,3:4,5:6}
for i in c:
    print(i,c[i])
#method 2
c={1:2,3:4,5:6}
for s,d in c.items():
    print(s,d)