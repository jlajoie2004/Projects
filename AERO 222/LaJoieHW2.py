from math import *
import numpy as np
import matplotlib.pyplot as plt

# Problem 1
print(f'Problem 1:')

def fx(x):
    fx = x**2 - e**x -np.arctan(x)
    return fx

def f1x(x):
    f1x = 2*x - e**x - 1/(x**2+1)
    return f1x

def f2x(x):
    f2x = 2 - e**x + (2*x)/((x**2+1)**2)
    return f2x

def newtonA(xk,fx,f1x):
    i = 1
    its = []
    resids = []
    xvals = []
    condition = True

    while condition:
        xvals.append(xk)
        xk1 = xk - fx(xk)/f1x(xk)
        xk = xk1

        resid = abs(fx(xk))
        resids.append(resid)
        if i > 1:
            condition = resid > 1e-8
        its.append(i)
        i += 1

    return xk1, i, resids, xvals, its

def newtonB(xk,fx,f1x):
    i = 1
    its = []
    errors = []
    xvals = []
    condition = True

    while condition:
        xvals.append(xk)
        xk1 = xk - fx(xk)/f1x(xk)
        xk = xk1

        error = abs(fx(xk))/abs(f1x(xk))
        errors.append(error)
        if i > 1:
            condition = abs(xk1 - xvals[-1]) < abs(xvals[-1] - xvals[-2])
        its.append(i)
        i += 1

    return xk1, i, errors, xvals, its

# Part A
root1, it1, resids1, xvals1, its1 = newtonA(0,fx,f1x)

print(f'Part A')
print(f'The final residual is {resids1[-1]}, the number of iterations is {it1}, and the root is {root1}')

# Part B
root2, it2, errors2, xvals2, its2 = newtonB(0,fx,f1x)

print(f'Part B:')
print(f'The final error is {errors2[-1]}, the number of iterations is {it2}, and the root is {root2}')

# Part C

x = np.linspace(-10,10,1000)
g1 = [abs(fx(x)*f2x(x)/f1x(x)**2) for x in x]
y1 = [1 for x in x]
plt.plot(x, g1, label = '|dg(x)|')
plt.plot(x, y1, label = 'y=1')
plt.xlabel('x')
plt.ylabel('|dg(x)|')
plt.title('Range of Convergence')
plt.show()

# Part D
print('Part D:')

def err_n(x):
    err_n = []
    for i in range(len(x)-1):
        err_n.append(abs(x[i]-x[-1]))
    return err_n

errn = err_n(xvals2)

def convergenceRate(errors):
    e1 = errors[-4]
    e2 = errors[-3]
    e3 = errors[-2]
    numerator = np.log(e3) - np.log(e2)
    denominator = np.log(e2) - np.log(e1)
    return numerator/denominator

def errorConstant(errors,alpha):
    e1 = errors[-3]
    e2 = errors[-2]
    return e2/e1**alpha

alpha = convergenceRate(errn)
lam = errorConstant(errn,alpha)

print(f'Order of convergence is {alpha} and the asymptotic error constant is {lam}')

# Problem 4
print(f'\nProblem 4:')

def gx(x):
    gx = (np.log(1.364)*(x-1))/(log(1+(.78**2)*(x-1)/2))
    return gx

def fixedpoint(xk,gx):
    i = 1
    xvals = []
    condition = True

    while condition:
        xvals.append(xk)
        xk1 = gx(xk)
        xk = xk1

        if i > 1:
            condition = abs(xk1 - xvals[-1]) < abs(xvals[-1] - xvals[-2])

        i += 1

    return xk1, i

root3, its3 = fixedpoint(0,gx)

print(f'I used the Fixed-point Method, my initial guess was 0, and my g(x) is '
      f'\n(ln(1.364)*(x-1))/(ln(1+(.78**2)*(x-1)/2)) ')
print(f'The root is {round(root3,3)} and the number of iterations is {its3}')

# Problem 5
print(f'\nProblem 5:')

# Part A
def MatrixInvert(A):

    n = A.shape[0]

    I = np.eye(n)

    Ab = np.concatenate((A,I),axis=1)

    for col in range(n):

        pivot_row = col
        for i in range(col + 1,n):
            if abs(Ab[i][col]) > abs(Ab[pivot_row][col]):
                pivot_row = i
        Ab[[col,pivot_row]] = Ab[[pivot_row,col]]

        pivot = Ab[col][col]
        Ab[col] /= pivot

        for row in range(n):
            if row == col:
                continue
            m = Ab[row][col]
            Ab[row] = Ab[row] - m*Ab[col]

    A_inv = Ab[:,n:2*n]
    return A_inv

print(f'Part A:')
A = np.array([[3,2,7,-1,4],
              [6,-2,0,2,-2],
              [4,1,-1,2,4],
              [2,10,-6,-4,1],
              [5,3,-1,-8,3]])

print(f'Using Guass-Jordan Method A^-1 is:\n {MatrixInvert(A)}')
print(f'Using NumPy A^-1 is:\n {np.linalg.inv(A)}')
print(f'They are the same.')

# Part B
print(f'Part B:')

b = np.array([-1,3,5,-6,3])

x = np.dot(MatrixInvert(A),b)

print(f'The solution to Ax=b is {x}1111111111111ndw')