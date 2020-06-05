#Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: done
#9.0 2 4.5

a=0
b=0
while True:
  i=input()
  if i=='done':
    break
  try:
    y=float(i)
  except:
    print("invalid")
    continue
  a=a+y
  b=b+1
print(a,b,a/b)