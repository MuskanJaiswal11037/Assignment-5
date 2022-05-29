from telnetlib import XAUTH
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem
'''  QUESTION:-A telephone call occurs at random in the interval (0,1). In this experiment, the outcomes
are time distances t between 0 and 1and the probability that t is between t1 and t2
 is given by P{t1<=t<=t2}=t2-t1 .
 Find C.D.F of the given event.

ANSWER:- Let the random variable be x such that x(t) = t , 0<=t<=1
Let the distribution function be F1 for x>0, F2 for 0<=x<=1; F3 for x>0.

1. If x>1, then x(t)<=x.
F1 = P{X<=x} = P{0<=t<=1} = P(S) = 1-0=1
2. If 0<=x<=1, for every t in the interval (0,x).
F2 = P{X<=x} = P{0<=t<=x} = x-0 = x
3. If x<0,
F3 = 0, because t>=0.

'''

x = np.linspace(0,1.01,10)
y=x
x2=np.linspace(1,1.5,3)
y2=[1,1,1]

plt.subplot(1, 1, 1)
stem(x, y, linefmt='k--', markerfmt='ko', basefmt='k-')
stem(x2,y2,linefmt='k--', markerfmt='ko', basefmt='k-')
plt.xlabel('Value of Y')
plt.ylabel('Cumulative Distribution Function')
plt.xticks(x)

plt.grid()
plt.tight_layout()
plt.show()



