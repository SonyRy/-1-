import matplotlib.pyplot as plt
from random import randint
plt.figure()

model=[0 for i in range (1000)]
for j in range (1000):
    for i in range(1000):
        ind=randint(0,1)
        if ind==0:
            model[j]+=1
        else: model[j]-=1


plt.hist(model,50)
plt.show()