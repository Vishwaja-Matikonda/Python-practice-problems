#reading whole data of a file into a string
str=open("hello.txt")
s=str.read()
print(len(s))
print(s[:12])
if 'BYE' in s:
  print("yes")
else:
    print("no")