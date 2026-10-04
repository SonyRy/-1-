import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('iris_data.csv')

SepalWidthCm=list(df['SepalWidthCm'])
SepalWidthCm1=SepalWidthCm[:50]
SepalWidthCm2=SepalWidthCm[50:100]
SepalWidthCm3=SepalWidthCm[100:]

SepalLengthCm=list(df['SepalLengthCm'])
SepalLengthCm1=SepalLengthCm[:50]
SepalLengthCm2=SepalLengthCm[50:100]
SepalLengthCm3=SepalLengthCm[100:]

PetalLengthCm=list(df['PetalLengthCm'])
PetalLengthCm1=PetalLengthCm[:50]
PetalLengthCm2=PetalLengthCm[50:100]
PetalLengthCm3=PetalLengthCm[100:]

PetalWidthCm=list(df['PetalWidthCm'])
PetalWidthCm1=PetalWidthCm[:50]
PetalWidthCm2=PetalWidthCm[50:100]
PetalWidthCm3=PetalWidthCm[100:]


fig = plt.figure(figsize = (20,10))
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)


ax1.set_title('SepalLength&SepalWidthCm')
ax1.scatter(SepalWidthCm1, SepalLengthCm1, s=6, c='blue')
ax1.scatter(SepalWidthCm2, SepalLengthCm2, s=6, c='red')
ax1.scatter(SepalWidthCm3, SepalLengthCm3, s=6, c='green')


ax2.set_title('SepalLength&PetalWidthCm')
z2 = np.polyfit(SepalLengthCm, PetalWidthCm, 1)
p2 = np.poly1d(z2)
ax2.plot(SepalLengthCm, p2(SepalLengthCm), c='black',linewidth=0.5)
print(p2)
ax2.scatter(SepalLengthCm1, PetalWidthCm1, s=6, c='blue')
ax2.scatter(SepalLengthCm2, PetalWidthCm2, s=6, c='red')
ax2.scatter(SepalLengthCm3, PetalWidthCm3, s=6, c='green')


ax3.set_title('SepalWidth&PetalWidthCm')
ax3.scatter(SepalWidthCm1, PetalWidthCm1, s=6, c='blue')
ax3.scatter(SepalWidthCm2, PetalWidthCm2, s=6, c='red')
ax3.scatter(SepalWidthCm3, PetalWidthCm3, s=6, c='green')

ax4.set_title('PetalLength&SepalLengthCm')
z4 = np.polyfit(PetalLengthCm, SepalLengthCm, 1)
p4 = np.poly1d(z4)
ax4.plot(PetalLengthCm, p4(PetalLengthCm), c='black',linewidth=0.5)
print(p4)
ax4.scatter(PetalLengthCm1, SepalLengthCm1, s=6, c='blue')
ax4.scatter(PetalLengthCm2, SepalLengthCm2, s=6, c='red')
ax4.scatter(PetalLengthCm3, SepalLengthCm3, s=6, c='green')

ax5.set_title('PetalLength&PetalWidthCm')
z5 = np.polyfit(PetalLengthCm, PetalWidthCm, 1)
p5 = np.poly1d(z5)
ax5.plot(PetalLengthCm, p5(PetalLengthCm), c='black',linewidth=0.5)
print(p5)
ax5.scatter(PetalLengthCm1, PetalWidthCm1, s=6, c='blue')
ax5.scatter(PetalLengthCm2, PetalWidthCm2, s=6, c='red')
ax5.scatter(PetalLengthCm3, PetalWidthCm3, s=6, c='green')


ax6.set_title('PetalLength&SepalWidthCm')
ax6.scatter(PetalLengthCm1, SepalWidthCm1, s=6, c='blue')
ax6.scatter(PetalLengthCm2, SepalWidthCm2, s=6, c='red')
ax6.scatter(PetalLengthCm3, SepalWidthCm3, s=6, c='green')

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()
plt.tight_layout()
fig.subplots_adjust(hspace=0.2, wspace=0.3)

plt.show()

