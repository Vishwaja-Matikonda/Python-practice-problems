str = 'X-DSPAM-Confidence :0.8475'
a=str.find(':')
c=str[a+1:]
d=float(c)
print(d)
print(type(c))
string = 'X-DSPAM-confidence :0.8475'
position = string.find(':')
number = string[(position+1):]
floating_number = float(number)
print(floating_number)
print(type(floating_number))
