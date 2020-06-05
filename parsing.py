#parsing and extracting
s='from vishwaja.matikonda@gmail.com 5:40 PM'
a=s.find('v')
print(a)
b=s.find(' ',a)
print(b)
c=s[a:b]
print(c)