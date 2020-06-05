# t=open('file1.txt')
# for i in t:
#     i.rstrip()
#     a=i.split()
#     print(a[2])
#
# han = open ('file1.txt')
# for line in han:
#      line = line.rstrip()
#      wds = line.split()
#      if wds[0]!='From' :
#           continue
#      print(wds[2])


han = open ('file1.txt')
for line in han:
     line = line.rstrip()
     wds = line.split()
     if len(wds)<3 or wds[0]!='From' :
          continue
     print(wds[2])