import matplotlib.pyplot as p
import numpy as np
import sympy as sym
import math
import cmath
#Steps:
#1)Locate the open loop poles and zeros in the ‘s’ plane
#2)Find the number of root locus branches.
#3)Identify and draw the real axis root locus branches
#4)Find the centroid and the angle of asymptotes.
#5)Find the intersection points of root locus branches with an imaginary axis.
#6)Find Break-away and Break-in points.
#7) Find the angle of departure and the angle of arrival.
          #then plot root locus
#angle of asymp
angle1 = ((2*0+1)/4)*180
angle2 = ((2*1+1)/4)*180
#calculate centroid
centroid= (-25-50-50)/4
# intersection points of root locus branches with an imaginary axis.
line = np.linspace(-100,100,1000)
#function to get break in point
s = sym.symbols('sy')
func = s**4+125*s**3+5100*s**2+65000*s
diff_func = func.diff(s)
fn= sym.Poly(diff_func,s)
breakin= np.roots(fn.all_coeffs())
#routh
k = sym.symbols('k')
val = (4580*65000-125*k)/4580
solution = sym.solve(val)
fn = sym.Poly(4580*s**2+solution[0],s)
#departure angle
phi=180-math.degrees(math.atan(10/50)) + 90 + (180-math.degrees(math.atan(10/25)))
depangle = 180 - phi
#plot imajinary points 
imajpoints = np.roots(fn.all_coeffs())
 #plot poles on s plane
p.scatter([0,-25,-50,-50], [0,0,10,-10], label= "lb", color= "blue", marker= "x", s=50)
p.plot(line+centroid,line, color='red', linestyle='dashed', linewidth = 1)
p.plot(line+centroid,-line, color='red', linestyle='dashed', linewidth = 1)
p.scatter(breakin[2], 0, color= 'r', marker= ".", s=100)
p.scatter([0,0], [imajpoints[0].imag,imajpoints[1].imag], color= 'r', marker= ".", s=100)
for i in np.linspace(0,10000000,1000):
  a = sym.Poly(func+i, s)
  curves= np.roots(a.all_coeffs())
  for j in range(len(curves)):
      p.scatter([curves[j].real], [curves[j].imag], color= "green",  
            marker= "o", s=2)
 
p.axvline(0)
p.axhline(0)
p.show()
