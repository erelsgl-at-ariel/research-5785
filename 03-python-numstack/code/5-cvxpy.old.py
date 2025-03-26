import math 
from cvxpy import log


print("\nPROBLEM: ")
print("Three cakes have to be divided among 2 people with values:")
print("2 3 4")
print("8 7 6")

# Define x,y,z = the fraction of each region given to player 1.
x = cvxpy.Variable()
y = cvxpy.Variable()
z = cvxpy.Variable()

print("\nMaximize the sum of logs:")
prob = cvxpy.Problem(
    objective   =  cvxpy.Maximize(log(2*x + 3*y + 4*z) + log(8*(1-x)+7*(1-y)+6*(1-z))),
    constraints = [0 <= x, x <= 1, 0<= y , y <= 1, 0 <= z, z <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal product", math.exp(prob.value))
print("optimal x", round(float(x.value),5))
print("optimal y", round(float(y.value),5))
print("optimal z", round(float(z.value),5))