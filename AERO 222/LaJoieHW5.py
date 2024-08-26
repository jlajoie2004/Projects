import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy

# Homework 5
# Problem 1

exactI = (3/13)*(1+np.exp(-3*np.pi/2))
def f(x):
    f = np.exp(-3*x)*np.cos(2*x)
    return f

def mid(n):
    h = (np.pi/2)/n

    sumf = 0
    for i in range(n):
        xmid = (i+.5)*h
        sumf += f(xmid)

    I = h*sumf
    return I

def trap(n):
    h = (np.pi/2)/n

    sumf = .5*(f(np.pi/2) + f(0))
    for i in range(1,n):
        sumf += f(i*h)

    I = h*sumf
    return I

nvals = np.linspace(10,50,40)

midpoint = np.zeros(len(nvals))
trapezoid = np.zeros(len(nvals))
for i in range(len(nvals)):
    midpoint[i] = mid(int(nvals[i]))
    trapezoid[i] = trap(int(nvals[i]))


plt.plot(nvals,midpoint,"b-",label = "Midpoint Method")
plt.plot(nvals,trapezoid,"r-",label = "Trapezoid Method")
plt.xlabel("Number of Partitions")
plt.ylabel("Integral Value")
plt.legend()
plt.show()

mid_error = abs(midpoint - exactI)
trap_error = abs(trapezoid-exactI)

plt.semilogy(nvals,mid_error,"b-",label = "Midpoint Error")
plt.semilogy(nvals,trap_error,"r-",label = "Trapezoid Error")
plt.xlabel("Number of Partitions")
plt.ylabel("Absolute Error")
plt.legend()
plt.show()

# Problem 2:

def f(x):
    f = 2000*np.log(110000/(110000-1600*x)) - 9.8*x
    return f

def gaussleg(a,b,n,f):
    x, w = np.polynomial.legendre.leggauss(n)
    sum = 0

    for i in range(n):
        sum += w[i] * f(((b-a)/2)*(x[i]+1)+a)

    int = ((b-a)/2) * sum

    return int

gl_4 = gaussleg(5,30,4,f)
gl_6 = gaussleg(5,30,6,f)
gl_8 = gaussleg(5,30,8,f)

print(f'The value of the integral using 4 point Gauss_Legendre is {gl_4}\n'
      f'The value of the integral using 6 point Gauss_Legendre is {gl_6}\n'
      f'The value of the integral using 8 point Gauss_Legendre is {gl_8}')

# Problem 3:
def f1(x,y):
    f1 = x**2 -1
    return f1

def f2(x,y):
    f2 = -3*x*y
    return f2

def eulers(a,b,n,y0,f):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    h = (b-a)/n


    x[0] = a
    y[0] = y0

    for i in range(n):
        x[i+1] = x[i]+h
        y[i+1] = y[i] + h*f(x[i],y[i])

    return x,y

def avgEulers(a,b,n,y0,f):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    h = (b-a)/n

    x[0] = a
    y[0] = y0

    for i in range(n):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + (h/2)*(f(x[i],y[i])+f(x[i]+h,y[i]+h*f(x[i],y[i])))

    return x,y

def midEulers(a,b,n,y0,f):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    h = (b-a)/n

    x[0] = a
    y[0] = y0

    for i in range(n):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*f(x[i]+h/2,y[i]+(h/2)*f(x[i],y[i]))

    return x,y

# For Equation 1:

x30, y1_30 = eulers(0,5,30,1,f1)
x30, y2_30 = avgEulers(0,5,30,1,f1)
x30, y3_30 = midEulers(0,5,30,1,f1)

ytrue30 = (1/3)*x30**3-x30+1

x300, y1_300 = eulers(0,5,300,1,f1)
x300, y2_300 = avgEulers(0,5,300,1,f1)
x300, y3_300 = midEulers(0,5,300,1,f1)

ytrue300 = (1/3)*x300**3-x300+1

nvals30 = np.linspace(0,5,31)
error1_30 = abs(ytrue30-y1_30)
error2_30 = abs(ytrue30-y2_30)
error3_30 = abs(ytrue30-y3_30)

nvals300 = np.linspace(0,5,301)
error1_300 = abs(ytrue300-y1_300)
error2_300 = abs(ytrue300-y2_300)
error3_300 = abs(ytrue300-y3_300)

plt.plot(x30,y1_30,label = "Eulers Method")
plt.plot(x30,y2_30,label = "Average Derivative Eulers")
plt.plot(x30,y3_30,label = "Midpoint Derivative Eulers")
plt.plot(x300,ytrue300,label = "True Value")
plt.title("Equation 1 Methods (30 Iterations)")
plt.legend()
plt.show()

plt.plot(x300,y1_300,label = "Eulers Method")
plt.plot(x300,y2_300,label = "Average Derivative Eulers")
plt.plot(x300,y3_300,label = "Midpoint Derivative Eulers")
plt.plot(x300,ytrue300,label = "True Value")
plt.title("Equation 1 Methods (300 Intervals)")
plt.legend()
plt.show()

plt.semilogy(nvals30,error1_30,label = "Eulers Error (30 Intervals)")
plt.semilogy(nvals30,error2_30,label="Average Eulers Error (30 Intervals)")
plt.semilogy(nvals30,error3_30,label="Midpoint Eulers Error (30 Intervals)")
plt.semilogy(nvals300,error1_300,label = "Eulers Error (300 Intervals)")
plt.semilogy(nvals300,error2_300,label="Average Eulers Error (300 Intervals)")
plt.semilogy(nvals300,error3_300,label="Midpoint Eulers Error (300 Intervals)")
plt.legend()
plt.title("Equation 1 Errors")
plt.show()

# For Equation 2:

x30, y1_30 = eulers(1,3,30,2,f2)
x30, y2_30 = avgEulers(1,3,30,2,f2)
x30, y3_30 = midEulers(1,3,30,2,f2)

ytrue30 = 2*np.exp((-3/2)*(x30**2-1))

x300, y1_300 = eulers(1,3,300,2,f2)
x300, y2_300 = avgEulers(1,3,300,2,f2)
x300, y3_300 = midEulers(1,3,300,2,f2)

ytrue300 = 2*np.exp((-3/2)*(x300**2-1))

nvals30 = np.linspace(1,3,31)
error1_30 = abs(ytrue30-y1_30)
error2_30 = abs(ytrue30-y2_30)
error3_30 = abs(ytrue30-y3_30)

nvals300 = np.linspace(1,3,301)
error1_300 = abs(ytrue300-y1_300)
error2_300 = abs(ytrue300-y2_300)
error3_300 = abs(ytrue300-y3_300)

plt.plot(x30,y1_30,label = "Eulers Method")
plt.plot(x30,y2_30,label = "Average Derivative Eulers")
plt.plot(x30,y3_30,label = "Midpoint Derivative Eulers")
plt.plot(x300,ytrue300,label = "True Value")
plt.title("Equation 2 Methods (30 Iterations)")
plt.legend()
plt.show()

plt.plot(x300,y1_300,label = "Eulers Method")
plt.plot(x300,y2_300,label = "Average Derivative Eulers")
plt.plot(x300,y3_300,label = "Midpoint Derivative Eulers")
plt.plot(x300,ytrue300,label = "True Value")
plt.title("Equation 2 Methods (300 Iterations)")
plt.legend()
plt.show()

plt.semilogy(nvals30,error1_30,label = "Eulers Error (30 Intervals)")
plt.semilogy(nvals30,error2_30,label="Average Eulers Error (30 Intervals)")
plt.semilogy(nvals30,error3_30,label="Midpoint Eulers Error (30 Intervals)")
plt.semilogy(nvals300,error1_300,label = "Eulers Error (300 Intervals)")
plt.semilogy(nvals300,error2_300,label="Average Eulers Error (300 Intervals)")
plt.semilogy(nvals300,error3_300,label="Midpoint Eulers Error (300 Intervals)")
plt.legend()
plt.title("Equation 2 Errors")
plt.show()

# Problem 4:

# Part A

def rkutta(a,b,y0,n,f):
    y = y0
    h = (b-a)/n
    yvals = np.zeros(n+1)
    xvals = np.zeros(n+1)
    yvals[0] = y0
    xvals[0] = a

    for i in range(1,n+1):
        k1 = h*f(a,y)
        k2 = h*f(a+h/2, y+k1/2)
        k3 = h*f(a+h/2, y+k2/2)
        k4 = h*f(a+h, y+k3)

        y = y + (1/6)*(k1+2*k2+2*k3+k4)
        a = a+h

        xvals[i] = a
        yvals[i] = y

    return xvals, yvals

# For Equation 1:

x30, y1_30 = rkutta(0,5,1,30,f1)
x300, y1_300 = rkutta(0,5,1,300,f1)

sci30 = scipy.integrate.solve_ivp(f1,[0,5],[1],t_eval = x30).y[0]
sci300 = scipy.integrate.solve_ivp(f1,[0,5],[1],t_eval = x300).y[0]

ytrue30 = (1/3)*x30**3 - x30 + 1
ytrue300 = (1/3)*x300**3 - x300 + 1

error1_30 = abs(ytrue30 - y1_30)
error1_300 = abs(ytrue300 - y1_300)
errorsci_30 = abs(ytrue30 - sci30)
errorsci_300 = abs(ytrue300 - sci300)

plt.plot(x30,y1_30,label="30 Intervals")
plt.plot(x300,y1_300,label="300 Intervals")
plt.plot(x30,sci30,label="SciPy 30 Intervals")
plt.plot(x300,sci300,label="SciPy 300 Intervals")
plt.plot(x300,ytrue300,label="True Value")
plt.title("Runge Kutta Method for Equation 1")
plt.legend()
plt.show()

plt.semilogy(x30,error1_30,label="30 Intervals")
plt.semilogy(x300,error1_300,label="300 Intervals")
plt.semilogy(x30,errorsci_30, label="SciPy 30 Intervals")
plt.semilogy(x300,errorsci_300,label="SciPy 300 Intervals")
plt.title("Errors for Equation 1")
plt.legend()
plt.show()

# For Equation 2:

x30, y2_30 = rkutta(1,3,2,30,f2)
x300, y2_300 = rkutta(1,3,2,300,f2)

sci2_30 = scipy.integrate.solve_ivp(f2,[1,3],[2],t_eval = np.linspace(1,3,31)).y[0]
sci2_300 = scipy.integrate.solve_ivp(f2,[1,3],[2],t_eval = np.linspace(1,3,301)).y[0]

y2true30 = 2*np.exp((-3/2)*(x30**2-1))
y2true300 = 2*np.exp((-3/2)*(x300**2-1))

error2_30 = abs(y2true30 - y2_30)
error2_300 = abs(y2true300 - y2_300)
errorsci2_30 = abs(y2true30 - sci2_30)
errorsci2_300 = abs(y2true300 - sci2_300)

plt.plot(x30,y2_30,label="30 Intervals")
plt.plot(x300,y2_300,label="300 Intervals")
plt.plot(x30,sci2_30,label="SciPy 30 Intervals")
plt.plot(x300,sci2_300,label="SciPy 300 Intervals")
plt.plot(x300,y2true300,label="True Value")
plt.title("Runge Kutta Method for Equation 2")
plt.legend()
plt.show()

plt.semilogy(x30,error2_30,label="30 Intervals")
plt.semilogy(x300,error2_300,label="300 Intervals")
plt.semilogy(x30,errorsci2_30, label="SciPy 30 Intervals")
plt.semilogy(x300,errorsci2_300,label="SciPy 300 Intervals")
plt.title("Errors for Equation 2")
plt.legend()
plt.show()



