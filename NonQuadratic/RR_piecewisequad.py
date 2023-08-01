# The function that we optimize is piecewise quadratic with linear variation

import numpy as np
import random
# import multiprocessing

sF=1.0
d=100
n = 800 # should be even
L = 1
u = 0.1

points = np.random.normal(0,1/np.sqrt(d),[n,d])
norms=np.linalg.norm(points,2,1)
norms=np.expand_dims(norms,1)
points= points/norms
# print(points)

mean = np.mean(points,0)
zeros = np.zeros(d)
x_star = np.maximum(mean, zeros)/L + np.minimum(mean, zeros)/u

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
  print(np.median(e1), np.median(e2))
  return [np.median(e1), d1, np.median(e2), d2, K]


def randomReshuffle(eta, n, K):
  x=x_star+np.random.normal(0,1/np.sqrt(d))
  # r = np.random.permutation(points)
  # r=np.concatenate((-np.ones(int(n/2)), np.ones(int(n/2))))
  # random.shuffle(r)
  for i in range(1, K+1):
    r = np.random.permutation(points)
    for j in range(0, n):
      x = x - eta*(L*np.maximum(x, 0) + u*np.minimum(x, 0)) + eta*r[j]
  error = np.linalg.norm(x-x_star)
  return error**2 

def randomReshuffle_Flipping(eta, n, K):
  x=x_star+np.random.normal(0,1/np.sqrt(d))
  # r=np.concatenate((-np.ones(int(n/2)), np.ones(int(n/2))))
  # random.shuffle(r)
  for i in range(1, int(K/2)+1):
    r = np.random.permutation(points)
    for j in range(0, n):
      x = x - eta*(L*np.maximum(x, 0) + u*np.minimum(x, 0)) + eta*r[j]
    for j in range(0, n):
      x = x - eta*(L*np.maximum(x, 0) + u*np.minimum(x, 0)) + eta*r[n-1-j]
  error = np.linalg.norm(x-x_star)
  return error**2 


reps = 10
K_beg=30 # should be evenA
K_end=300
x_list=[]
l1=[];l2=[]
# pool = multiprocessing.Pool(1)
K_range = range(K_beg,K_end,4)
results=[]
for k in K_range:
  results.append(parallelOptimization(k))

f = open('plotdatanew/RR_piecewisequad_u0.1', 'w') # Replace with desired output file name
f.write("\n".join([",".join([str(r) for r in res]) for res in results]))
