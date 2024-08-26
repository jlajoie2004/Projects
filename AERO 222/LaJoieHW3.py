from math import *
import matplotlib.pyplot as plt
import numpy as np

# Problem 1

x = np.linspace(-.5,1.5,100)
y = np.cos(3*x)

y_meas = np.cos(3*x) + np.random.normal(0,.12,100)

A1 = np.vstack([np.ones(len(x)),x,2*x**2-1,4*x**3-3*x]).T
c1 = np.linalg.pinv(A1) @ y

A2 = np.vstack([(np.cos(x))**2,1-2*np.sin(x),np.cos(3*x)*np.sin(x),(3-x)/(3+x)]).T
c2 = np.linalg.pinv(A2) @ y

y_hat1 = c1[0] + c1[1]*x + c1[2]*(2*x**2-1) + c1[3]*(4*x**3-3*x)
y_hat2 = c2[0]*np.cos(x)**2 + c2[1]*(1-2*np.sin(x)) + c2[2]*(np.cos(3*x)*np.sin(x)) + c2[3]*((3-x)/(3+x))

plt.plot(x,y,'r-', label = 'Data Points')
plt.plot(x,y_meas,'b-',label = 'Data Points with noise')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

plt.plot(x,y_meas,'r-',label = 'Data Points with noise')
plt.plot(x,y_hat1,'b-',label = 'Line of Best Fit 1')
plt.plot(x,y_hat2,'g-',label = 'Line of Best Fit 2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

resid1 = y_hat1 - y_meas
resid2 = y_hat2 - y_meas

l1_norm1 = np.linalg.norm(resid1,ord=1)
l2_norm1 = np.linalg.norm(resid1,ord=2)
linf_norm1 = np.linalg.norm(resid1,ord=np.inf)

l1_norm2 = np.linalg.norm(resid2,ord=1)
l2_norm2 = np.linalg.norm(resid2,ord=2)
linf_norm2 = np.linalg.norm(resid2,ord=np.inf)

print(f'Problem 1:')
print(f'For yhat1, the L1 norm is {l1_norm1}, the L2 norm is {l2_norm1}, '
      f'and the Linf norm is {linf_norm1}')
print(f'For yhat1, the L1 norm is {l1_norm2}, the L2 norm is {l2_norm2}, '
      f'and the Linf norm is {linf_norm2}')

# Problem 2

t = np.linspace(0,5,100)

x = np.exp(-t)*np.cos(t)
x_meas = x + np.random.normal(0,.05,100)*np.sqrt(t)

W = np.diag(1/(1+0.1**(2.5-t)))
A = np.vstack([np.ones(len(t)),t,2*t**2-1,4*t**3-3*t]).T

c = np.linalg.inv(A.T @ W @ A) @ A.T @ W @ x
x_hat = c[0] + c[1]*t + c[2]*(2*t**2-1) + c[3]*(4*t**3-3*t)

plt.plot(t,x,'r-', label = 'Data Points')
plt.plot(t,x_meas,'b-',label = 'Data Points with noise')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

plt.plot(t,x_meas,'b-',label = 'Data Points with noise')
plt.plot(t,x_hat,'r-',label = 'Line of Best Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Problem 4

def f(x,P):
      y = 12 - P[1]*x**2 - np.exp(-P[3]*x**2)*np.sin(P[2]*x)+P[0]*(P[1]*P[3]-P[2]*x)
      return y

def j(x,P):
      j = np.array([(P[1]*P[3]-P[2]*x),-x**2+P[0]*P[3],
                    -x*np.exp(-P[3]*x**2)*np.cos(P[2]*x),
                    x**2*np.exp(-P[3]*x**2)*np.sin(P[2]*x)+P[0]*P[1]]).T
      return j

P_true = [-2,1,-1,5]
x = np.linspace(-1,1,100)

y_meas = f(x,P_true) + np.random.normal(0,.1,100)

P0 = [-2.2,.3,-1,5.2]
tol = 1e-6
i = 0

resid0 = f(x,P0) - y_meas

L2Norm_hist = []

for i in range(1, 101):
    P = P0 - np.linalg.inv(j(x,P0).T @ j(x,P0))@j(x,P0).T @ resid0
    resid1 = f(x,P) - y_meas
    residVect = abs(resid0 - resid1)

    i += 1
    P0 = P
    resid0 = resid1

    L2Norm = np.linalg.norm(residVect)
    L2Norm_hist.append(L2Norm)

    if L2Norm < tol:
        break
    if i == 100:
        print(f'Did not converge within 100 iterations')

iter = np.arange(1,i)

plt.plot(iter,L2Norm_hist,'b-')
plt.xlabel('Iterations')
plt.ylabel('L2 Norm of the Residual Vector')
plt.show()

# Problem 5

x = np.linspace(0,4,100)
y = (1 + x)/(np.sin(x/2)+np.exp(-x))

def L2(x):
    l0 = 1
    l1 = x

    l2 = (3/2)*x*l1 - (1/2)*l0

    return l2

def L3(x):
    l1 = 1
    l2 = L2(x)

    l3 = (5/3)*x*l2 - (2/3)*l1

    return l3

A = np.vstack([np.ones(len(x)),x,L2(x),L3(x)]).T
c = np.linalg.inv(A.T@A) @A.T@y

y_hat = c[0]*1 + c[1]*x + c[2]*L2(x) + c[3]*L3(x)

resid = y_hat - y
residNorm = np.linalg.norm(resid)
print(f'Problem 5:')
print(f'The L2 norm of the residual vector y is {residNorm}')

# Problem 6

def f(p):
    f1 = p[0]*p[1] - np.sin(p[2]) - np.pi
    f2 = p[0]*p[2]**3 + p[1]**2
    f3 = p[0]*p[1]*p[2] + p[0] + p[1] + p[2] + 1
    fVect = np.array((f1,f2,f3), dtype = float)

    return fVect

def j(p):
    j = np.array([[p[1],p[0],-np.cos(p[2])],
                 [p[2]**3,2*p[1],3*p[0]*p[2]**2],
                 [p[1]*p[2]+1,p[0]*p[2]+1,p[0]*p[1]+1]], dtype = float)
    return j

p0 = np.array([2,1,-1], dtype = float)
normHist = []
for i in range(1,16):
    j_inv = np.linalg.inv(j(p0))

    p = p0 - j_inv@f(p0)
    p0 = p

    res = f(p)
    resNorm = np.linalg.norm(res)
    normHist.append(resNorm)

iter = np.arange(1,16)
plt.semilogy(iter,normHist)
plt.xlabel('Iterations')
plt.ylabel('L2 Norm of the Residual')
plt.show()



