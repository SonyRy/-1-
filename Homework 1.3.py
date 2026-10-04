import matplotlib.pyplot as plt
from random import randint
plt.figure()
plt.title('Среднеквадратичное отклонение')
num=[i+1 for i in range (1000)]
srq=[0 for i in range (1000)]
model=[0 for i in range (1000)]
for j in range (1000):
    ind = [0]*(j+1)
    for i in range(j+1):
        ind[i]=randint(0,1)
        if ind[i]==0:
            model[j]+=1
        else: model[j]-=1
    model[j]=model[j]/(j+1)
    for i in range(j+1):
        srq[j]+=(ind[i]-model[j])**2
    srq[j]=(srq[j]/(j+1))**0.5
plt.grid()
plt.scatter(num,srq,s=1)
plt.show()