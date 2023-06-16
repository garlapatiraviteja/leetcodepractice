import numpy as np

#taking example of f(x)= 2x^2

def f(x):
  return 2*x**2

# the above caluclation is only 2 points 

x=np.arrange(0,5,0.001)  #arrange(start,stop,step) will be smoother line

y=f(x)

x1=2
p2_delta= 0.001

x2= x1+p_delta

y1=f(x1)
y2=f(x2)

approx_derviative = (y2-y1)/(x2-x1)  ### finding slope where we can find the impact of x in y

b= y2- approx_derivate*x2


def tangent_line(x):
  return approx_derivative * x2


print(f'where x={x1} is approx derovative {approx_derivative}')





# the above caluclation is only 5 different points

import numpy as np

#taking example of f(x)= 2x^2

def f(x):
  return 2*x**2



x=np.arrange(0,5,0.001)  #arrange(start,stop,step) will be smoother line

y=f(x)

for i in range(5)
  x1=i
  p2_delta= 0.001

  x2= x1+p_delta

  y1=f(x1)
  y2=f(x2)

  approx_derviative = (y2-y1)/(x2-x1)  ### finding slope where we can find the impact of x in y

  b= y2- approx_derivate*x2


  def tangent_line(x):
    return approx_derivative * x2


  print(f'where x={x1} is approx derovative {approx_derivative}')

