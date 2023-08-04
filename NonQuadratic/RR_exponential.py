# The function that we optimize is (1/6)|x|^3 with linear variation

import numpy as np
import random
# import multiprocessing

sF=100.0
print("SF: " + str(sF))
d=100
n = 800 # should be even
L = 100
u = 1
kappa = L/u
c = 0.5*np.log(kappa)
b = (u*L)**0.5/(c**2)
a = b*c

points = np.random.normal(0,1/np.sqrt(d),[n,d])
norms=np.linalg.norm(points,2,1)
norms=np.expand_dims(norms,1)
points= points/norms
# print(points)

mean = np.mean(points,0)
x_star = (1/c)*np.log([(1+i/a) for i in mean])

def parallelOptimization(K):
  print( K)
  # pid = multiprocessing.current_process()._identity[0]
  # RandomState(pid+K)

  stepFactor=sF
  eta = stepFactor * np.log(n*K) / (n*K*u)
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

def F(x):
  return sum(np.abs(x)**3)/3 - sum(mean*x)

F_star = F(x_star)
print("F_star = " + str(F_star))

def randomReshuffle(eta, n, K):
  x=x_star+np.random.normal(0,1/np.sqrt(d))
  for i in range(1, K+1):
    r = np.random.permutation(points)
    for j in range(0, n):
      #x = (1 - eta)*x + eta*r[j] # The gradient step.
      x = x - eta*(a*np.exp([c*i for i in x]) - a - r[j])
  error = np.linalg.norm(x-x_star)
  return error**2

def randomReshuffle_Flipping(eta, n, K):
  x=x_star+np.random.normal(0,1/np.sqrt(d))
  for i in range(1, int(K/2)+1):
    r = np.random.permutation(points)
    for j in range(0, n):
      # x = (1 - eta)*x + eta*r[j] # The gradient step.
      x = x - eta*(a*np.exp([c*i for i in x]) - a - r[j])
    for j in range(0, n):
      # x = (1 - eta)*x + eta*r[n-1-j] # The gradient step.
      x = x - eta*(a*np.exp([c*i for i in x]) - a - r[n-1-j])
  error = np.linalg.norm(x-x_star)
  return error**2


reps = 10

K_1 = [i for i in range(30, 100, 4)]
K_2 = [i for i in range(100, 500, 10)]
K_3 = [i for i in range(500, 1000, 50)]
K_range = K_1 + K_2 + K_3

K_beg=30 # should be even
K_end=100
x_list=[]
l1=[];l2=[]
# pool = multiprocessing.Pool(1)
# K_range = range(K_beg,K_end,4)
results=[]
for k in K_range:
  results.append(parallelOptimization(k))

f = open('plotdatanew/RR_exponential', 'w') # Replace with desired output file name
f.write("\n".join([",".join([str(r) for r in res]) for res in results]))
