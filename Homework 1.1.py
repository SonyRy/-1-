import matplotlib.pyplot as plt
from random import randint
fig=plt.figure()
s =[0 for i in range(1001)]
d=[i for i in range (1001)]
for i in range(1001):
    if i>0:
        ind=randint(0,1)
        if ind==1: s[i]=s[i-1]+1
        else:
           s[i]=s[i-1]-1
plt.plot(d, s)

plt.show()
