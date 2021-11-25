# The function that we optimize is $F(x)=\frac{1}{n}\sum_{i=1}^n f_i(x)$, where $f_i(x) = \frac{x^2}{2} - x$ if $i\leq n/2$, and $f_i(x) = x$ otherwise.

import numpy as np
# import multiprocessing

sF=2.0

def parallelOptimization(K):
  print(K)
  stepFactor=sF
  n = 800 # Should be even
  eta = stepFactor * np.log(n*K) / (n*K)
  e1 = []
  e2 = []
  for rep in range(reps):
    e1.append(IGD(eta, n, K))

  for rep in range(reps):
    e2.append(IGD_Flipping(eta, n, K))

  d1=np.percentile(e1, 75, interpolation = 'midpoint') - np.percentile(e1, 25, interpolation = 'midpoint')
  d2=np.percentile(e2, 75, interpolation = 'midpoint') - np.percentile(e2, 25, interpolation = 'midpoint')
  return [np.median(e1), d1, np.median(e2), d2, K]


def IGD(eta, n, K):
  x=0+np.random.normal(0,1)
    
  for i in range(1, K+1):  
    for j in range(0, int(n/2)):
      x = x - eta # The gradient step.

    for j in range(int(n/2), n):
      x = (1 - eta)*x + eta # The gradient step.
  return x**2 # Error is x**2, since the minimizer is x=0

def IGD_Flipping(eta, n, K):
  x=0+np.random.normal(0,1)
    
  for i in range(1, int(K/2)+1):

    for j in range(int(n/2), n):
      x = (1 - eta)*x + eta # The gradient step.

    for j in range(0, int(n/2)):
      x = x - eta # The gradient step.

    for j in range(0, int(n/2)):
      x = x - eta # The gradient step.

    for j in range(int(n/2), n):
      x = (1 - eta)*x + eta # The gradient step.




  return x**2 # Error is x**2, since the minimizer is x=0


reps = 10
K_beg=30 # should be even
K_end=300
x_list=[]
l1=[];l2=[];l3=[]
# pool = multiprocessing.Pool(16)
K_range = range(K_beg,K_end,4)
results=[]
for k in K_range:
  results.append(parallelOptimization(k))

f = open('plotdatanew/IGD', 'w') # Replace with desired output file name
f.write("\n".join([",".join([str(r) for r in res]) for res in results]))
