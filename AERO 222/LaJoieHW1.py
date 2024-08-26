from math import *
import numpy as np
import matplotlib.pyplot as plt

# Problem 1:
print(f'Problem 1:')
def f_x(x):
    fx = 2*x**2*sin(x/2) + 3*e**(4*(x-40)) - 5
    return fx
def f1_x(x):
    f1x = cos(x/2)*x**2 + 4*sin(x/2)*x + 12*e**(4*(x-40))
    return f1x

# Bisection Method

def bisection(f_x,f1_x,x0,x1,tol):
    bisec_list = []
    i = 0
    x_mid = (x0+x1)/2
    error = abs(f_x(x_mid))/abs(f1_x(x_mid))

    while error > tol:
        x_mid = (x0+x1)/2
        error = abs(f_x(x_mid))/abs(f1_x(x_mid))
        bisec_list.append(abs(f_x(x_mid)))
        if f_x(x_mid) * f_x(x0) > 0:
            x0 = x_mid
        else:
            x1 = x_mid

        i += 1

    return i, error, x_mid, bisec_list

b_it, b_error, b_root, b_list = bisection(f_x,f1_x,-4,4,10**(-8))

print(f'(Root, Error, Iterations) for the Bisection Method are: ({b_root},{b_error},{b_it})')

# Secant Method

def secant(f_x,f1_x,x0,x1,tol):
    secant_list = []
    i = 0
    error = abs(f_x(x1))/abs(f1_x(x1))

    while error > tol:
        x2 = x1 - (f_x(x1)*(x1 - x0))/(f_x(x1)-f_x(x0))
        x0 = x1
        x1 = x2

        error = abs(f_x(x1))/abs(f1_x(x1))
        secant_list.append(abs(f_x(x1)))
        i += 1

    return i, error, x1, secant_list

s_it, s_error, s_root, s_list = secant(f_x,f1_x,-4,4,10**(-8))

print(f'(Root, Error, Iterations) for the Secant Method are: ({s_root},{s_error},{s_it})')

# Regula_Falsi Method

def reg_falsi(f_x,f1_x,x0,x1,tol):
    rf_list = []
    i = 0
    error = abs(f_x(x1))

    while error > tol:
        x_rf = x1 - (f_x(x1)*(x1-x0))/(f_x(x1)-f_x(x0))
        error = abs(f_x(x_rf))
        rf_list.append(abs(f_x(x_rf)))

        if f_x(x_rf) * f_x(x0) > 0:
            x0 = x_rf
        else:
            x1 = x_rf

        i += 1

    return i, error, x_rf, rf_list

rf_it, rf_error, rf_root, rf_list = reg_falsi(f_x,f1_x,-4,4,10**(-8))

print(f'(Root, Error, Iterations) for the Regula-Falsi Method are: ({rf_root},{rf_error},{rf_it})')

plt.semilogy(b_list, label='Bisection Method')
plt.semilogy(s_list, label='Secant Method')
plt.semilogy(rf_list, label='Regula-Falsi Method')
plt.xlabel('Iteration Number')
plt.ylabel('|f(xn)|')
plt.legend()
plt.grid(True)
plt.show()

print(f'The Secant Method converged the fastest.')

# Problem 2:
print(f'Problem 2:')

def abs_error(x_true,x_est):
    error_abs = abs(x_true-x_est)
    return error_abs

def relative_error(x_true,x_est):
    error_relative = abs(x_true-x_est)/abs(x_true)
    return error_relative

# Part a:
print(f'Part A:')
def twoaf_x(x):
    twoaf_x = -20.31*x**3 + 16.66*x**2 - 21.73*x - 15.36
    return twoaf_x

def rounded2af(x,d):
    first = np.round(-20.31*np.round(x**3,decimals=d), decimals=d)
    second = np.round(16.66*np.round(x**2,decimals=d),decimals=d)
    third = np.round(-21.73*x,decimals=d)
    fourth = np.round(first+second+third-15.36,decimals=d)
    return fourth

print(f'With Machine Precision f(21.13) = {twoaf_x(21.13)}')
print(f'With rounding f(21.13) = {rounded2af(21.13,3)}')
print(f'The absolute error is {abs_error(twoaf_x(21.13),rounded2af(21.13,3))} '
      f'and the relative error is {relative_error(rounded2af(21.13,3),twoaf_x(21.13))}.')

# Part b
print(f'Part B:')

def twobf_x(x):
    twobf_x = ((-20.31*x + 16.66)*x - 21.73)*x - 15.36
    return twobf_x

def rounded2bf(x,d):
    first = np.round((np.round(np.round(-20.31*x,decimals=d)+16.66,decimals=d)*x),decimals=d)
    second = np.round((np.round(first - 21.73,decimals=d)*x),decimals=d)
    third = np.round(second - 15.36,decimals=d)
    return third

print(f'With Machine Precision f(21.13) = {twobf_x(21.13)}')
print(f'With rounding f(21.13) = {rounded2bf(21.13,3)}')
print(f'The absolute error is {abs_error(twobf_x(21.13),rounded2bf(21.13,3))} '
      f'and the relative error is {relative_error(rounded2bf(21.13,3),twobf_x(21.13))}.')

# Part c
print(f'Part C:')
print(f'Repeat of A:')
print(f'With Machine Precision f(21.13) = {twoaf_x(21.13)}')
print(f'With rounding f(21.13) = {rounded2af(21.13,5)}')
print(f'The absolute error is {abs_error(twoaf_x(21.13),rounded2af(21.13,5))} '
      f'and the relative error is {relative_error(rounded2af(21.13,5),twoaf_x(21.13))}.')
print(f'Repeat of B:')
print(f'With Machine Precision f(21.13) = {twobf_x(21.13)}')
print(f'With rounding f(21.13) = {rounded2bf(21.13,5)}')
print(f'The absolute error is {abs_error(twobf_x(21.13),rounded2bf(21.13,5))} '
      f'and the relative error is {relative_error(rounded2bf(21.13,5),twobf_x(21.13))}.')

# Problem 3:
print(f'Problem 3:')
true = 4.9787 * 10 **(-2)
# Part a
print(f'Part A:')
fx = 0
error_a =[]
for k in range(10):
    fx += (((-1)**k)*(3**k))/(factorial(k))
    error_a.append(abs(true - fx))

print(f'E^-3 to 5 digits of precision is {np.round(fx, decimals = 5)}')

# Part b
print(f'Part B:')
error_b = []
fxb_denom = 0
for k in range(10):
    fxb_denom += ((3**k)/factorial(k))
    error_b.append(abs(true - 1/fxb_denom))
fxb = 1/fxb_denom

print(f'E^-3 to 5 digits of precision is {np.round(fxb, decimals=5)}')
print(f'The formula for part b gives more accurate results.')
plt.semilogy(error_a, label='Error in Part A')
plt.semilogy(error_b, label='Error in Part B')
plt.xlabel('Iteration Number')
plt.ylabel('Absolute Error')
plt.legend()
plt.grid(True)
plt.show()