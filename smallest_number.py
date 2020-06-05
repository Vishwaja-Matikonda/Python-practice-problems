#Smallest number
sm=None
for i in [9,41,12,3,74,15,1]:
  if sm==None:
    sm=i
  elif i<sm:
    sm=i
print("smallest",sm)