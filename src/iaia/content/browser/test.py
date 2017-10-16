import random

num=[1,2,3,4,5,6,7,8,9,10]
ran=range(1,10)
result=random.sample(ran,5)
result.sort()

con=[{'title':1,'num':1},
    {'title':2,'num':1},
    {'title':3,'num':1},
    {'title':4,'num':1}]
con.remove(con[0])
print(con[0])