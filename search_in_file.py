#searching and printing the sequences starting with:: and also stripping the files
str=open('hello.txt')
for i in str:
    i=i.rstrip()
    if 'hii' in i:
      print(i)
print("\n")

#2
str = open('hello.txt')
for i in str:
    i = i.rstrip()
    if i.startswith('hii'):
        print(i)

#3
str = open('hello.txt')
for i in str:
    i = i.rstrip()
    if not i.startswith('hii'):
        continue
    print(i)


str = open('hello.txt')
for i in str:
    i = i.rstrip()
    if not i.startswith('hii'):
        print(i)
