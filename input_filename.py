#taking filename ass input
f=input("Enter the filename")
try:
    d=open(f)
except:
    print("cant open the file",f)
    quit()
count=0
for i in d:
    i = i.rstrip()
    if i.startswith('hii'):
        count = count + 1
print("there are ",count," of hi files in",f)
