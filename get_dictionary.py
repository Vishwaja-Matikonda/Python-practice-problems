#counting the number of words in a sentense
count={}
a=input("enter the text")
b=a.split()
print(b)
for i in b:
    count[i]=count.get(i,0)+1
print(count)