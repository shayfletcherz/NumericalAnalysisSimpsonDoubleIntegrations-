import matplotlib.pyplot as plt
# Plotting our given function i.e., surface
#(Plotting with sympy if we dont want to plot with numpy)
import sympy as sp
from sympy.plotting import plot3d

#Defining our function to integrate. We can replace to any valid function
def function(x, y):
    return y*x**2 + x*y**2

#Defining limits of integrations
#
#outer limits. i.e., y limits
y_0 = -1;              #lower limit
y_n = 1;               #Upper limit

#inner limits. i.e., x limits
x_0 = 1;               #lower limit
x_n = 2;               #upper limit

#Defining mesh grid points. Increase these values for better accuracy
ny = 40;               #Meshgrid points for x
nx = 40;               #Meshgrid points for y

#Calculating the step sizes
hx = (x_n - x_0)/nx    #step size for x values
hy = (y_n - y_0)/ny    #step size for y values

#We implement the algorithm for Simpson's 1/3 rule here
#Initial sum
sum = 0

for i in range(0,ny+1):               #Outer loop as dy is outer integration parameter
    if i==0 or i==ny:                 #Setting coefficients =1 for initial and final points
        w_y = 1 
    elif i%2!=0:                #Setting ceofficients = 4 for sum over odd indices
        w_y = 4
    else:
        w_y = 2                       #Setting coefficients = 2 for sum over even indices
    for j in range(0, nx+1):
        if j==0 or j==nx:
            w_x = 1 
        elif j%2!=0:
            w_x = 4
        else:
            w_x = 2
        x = x_0 + j*hx                       #changing x with increment of hx
        y = y_0 + i*hy                       #Changing y with increment of hy
        sum = sum + w_y * w_x * function(x, y)       # Repeating sum over indices i and j
Simp_int = hx*hy/9 *sum                      #Final Simpson's 1/3 rule

print('Simpsons Integration gives: ',Simp_int) #Final result print 

error_bound = 1/90*90 *hx**5 * hy**5           #Error bound print for Simpson's 1/3 rule
print('Error bound by assuming upper bound to be 1 is: ', error_bound)

x, y = sp.symbols('x y')
#View graphs
plot3d(function(x, y), title ='General given surface')
plot3d(function(x, y), (x, x_0, x_n), (y, y_0, y_n), title='Required surface for area calculation')