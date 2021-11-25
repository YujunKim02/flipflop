# The function that we optimize is $F(x)=\frac{1}{n}\sum_{i=1}^n f_i(x)$, where $f_i(x) = \frac{x^2}{2} - x$ if $i\leq n/2$, and $f_i(x) = \frac{x^2}{2} + x$ otherwise.

import numpy as np
import random
# import multiprocessing

sF=1.0
d=100
n = 800 # should be even

points = np.random.normal(0,1/np.sqrt(d),[n,d])
norms=np.linalg.norm(points,2,1)
norms=np.expand_dims(norms,1)
points= points/norms
# print(points)

mean = np.mean(points,0)

def parallelOptimization(K):
  print(K)
  # pid = multiprocessing.current_process()._identity[0]
  # RandomState(pid+K)

  stepFactor=sF
  eta = stepFactor * np.log(n*K) / (n*K)
  e1 = []
  e2 = []
  
  for rep in range(reps):
    e1.append(randomReshuffle(eta, n, K))

  for rep in range(reps):
    e2.append(randomReshuffle_Flipping(eta, n, K))

  
  d1=np.percentile(e1, 75, interpolation = 'midpoint') - np.percentile(e1, 25, interpolation = 'midpoint')
  d2=np.percentile(e2, 75, interpolation = 'midpoint') - np.percentile(e2, 25, interpolation = 'midpoint')
  return [np.median(e1), d1, np.median(e2), d2, K]


def randomReshuffle(eta, n, K):
  x=mean+np.random.normal(0,1/np.sqrt(d))
  # r = np.random.permutation(points)
  # r=np.concatenate((-np.ones(int(n/2)), np.ones(int(n/2))))
  # random.shuffle(r)
  for i in range(1, K+1):
    r = np.random.permutation(points)
    for j in range(0, n):
      x = (1 - eta)*x + eta*r[j] # The gradient step.
  error = np.linalg.norm(x-mean)
  return error**2 

def randomReshuffle_Flipping(eta, n, K):
  x=mean+np.random.normal(0,1/np.sqrt(d))
  # r=np.concatenate((-np.ones(int(n/2)), np.ones(int(n/2))))
  # random.shuffle(r)
  for i in range(1, int(K/2)+1):
    r = np.random.permutation(points)
    for j in range(0, n):
      x = (1 - eta)*x + eta*r[j] # The gradient step.
    for j in range(0, n):
      x = (1 - eta)*x + eta*r[n-1-j] # The gradient step.
  error = np.linalg.norm(x-mean)
  return error**2 




reps = 10
K_beg=30 # should be even
K_end=300
x_list=[]
l1=[];l2=[];l3=[]
# pool = multiprocessing.Pool(1)
K_range = range(K_beg,K_end,4)
results=[]
for k in K_range:
  results.append(parallelOptimization(k))

f = open('plotdatanew/RR', 'w') # Replace with desired output file name
f.write("\n".join([",".join([str(r) for r in res]) for res in results]))
