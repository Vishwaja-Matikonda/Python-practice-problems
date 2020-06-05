#reading a file
str=open("hello.txt")
count=0
for i in str:
    print(i)
    count=count+1
print(count)