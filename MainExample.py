"""
Author: Sina Anheyer
Year: 2025
Python Version: 3.9.7

This Code generates the main example using
the code of Hübner et. al provided for their paper:

'Spatial branch and bound for nonconvex separable piecewise
linear optimization'
--------------------------------------------------------
only a few necessary changes to provided implementation:
--------------------------------------------------------
added case distinction in sBB_functions_rules and sBB_main_rules for the different branching rules
added case distinction for infeasible subproblems in sBB_main_rules
added case distinction for longest edge - node selection changed to 'worst first approach' 
selecting the node with the largest lower bound first
this hopefully prevents the algorithm from loosing itself in the smallest lower bounds

sBB_functions_rules:
In getEnvelope I had to change:
------------------------------
points_x.insert(0,interval[0])
points_x.append(interval[1])
points_y.insert(0,interval_y[0])
points_y.append(interval_y[1])
------------------------------
to 
------------------------------
points_x = np.insert(points_x,0,interval[0])
points_x = np.append(points_x,interval[1])
points_y = np.insert(points_y,0,interval_y[0])
points_y = np.append(points_y,interval_y[1])
------------------------------
due to a syntax error
"""
import sBB_main_rules as sBB
import sBB_functions_rules as sBBf
import instance_generation as ig
import numpy as np
import matplotlib.pyplot as plt

#-----------------------#
# parameters
#-----------------------#
#termination gap
epsilon = 0.00001
#examples generated for approximations with the
#following amount of breakpoints
K1 = 2000 
K2 = 20
#timelimit
t = 10
#rhs
rhs = 4.2
#which two functions form the separable PLF
#I = [2,1]
I = [21,21]
#---------------------------------------------------------#
# step 1: aquire lists of breakpoints and function values
#---------------------------------------------------------#

[plf_breakpoints_x1,plf_breakpoints_y1] = ig.getPLFs(2,K1,I,False)
[plf_breakpoints_x2,plf_breakpoints_y2] = ig.getPLFs(2,K2,I,False)

#-----------------------#
# optimize with sBB
#-----------------------#

#optimize for K1 many breakpoints
#solutionK1_breakpoint    = sBB.spatialBB(plf_breakpoints_x1,plf_breakpoints_y1,2,K1,"knapsack",rhs,t,epsilon,"breakpoint")
solutionK1_longest_edge  = sBB.spatialBB(plf_breakpoints_x1,plf_breakpoints_y1,2,K1,"knapsack",rhs,t,epsilon,"longest edge")
solutionK1_largest_error = sBB.spatialBB(plf_breakpoints_x1,plf_breakpoints_y1,2,K1,"knapsack",rhs,t,epsilon,"largest error")

#optimize for K2 many breakpoints
#solutionK2_breakpoint    = sBB.spatialBB(plf_breakpoints_x2,plf_breakpoints_y2,2,K2,"knapsack",rhs,t,epsilon,"breakpoint")
solutionK2_longest_edge  = sBB.spatialBB(plf_breakpoints_x2,plf_breakpoints_y2,2,K2,"knapsack",rhs,t,epsilon,"longest edge")
solutionK2_largest_error = sBB.spatialBB(plf_breakpoints_x2,plf_breakpoints_y2,2,K2,"knapsack",rhs,t,epsilon,"largest error")
#-----------------------#
#  Print main results
#-----------------------#
print("------------------------")
print("for K1 many breakpoints:")
print("------------------------")
'''
print("Solution Time with breakpoint rule is: " + str(solutionK1_breakpoint[0]))
print("node count with breakpoint rule is: " + str(solutionK1_breakpoint[5]))
print("global uppper bound with breakpoint rule is: " + str(solutionK1_breakpoint[6]))
print("incumbent solution with breakpoint rule is: " + str(solutionK1_breakpoint[8]))
print("------------------------")
'''
print("Solution Time with longest edge rule is: " + str(solutionK1_longest_edge[0]))
print("node count with longest edge rule is: " + str(solutionK1_longest_edge[5]))
print("global uppper bound with longest edge rule is: " + str(solutionK1_longest_edge[6]))
print("incumbent solution with longest edge rule is: " + str(solutionK1_longest_edge[8]))
print("------------------------")
print("Solution Time with largest error rule is: " + str(solutionK1_largest_error[0]))
print("node count with largest error rule is: " + str(solutionK1_largest_error[5]))
print("global uppper bound with largest error rule is: " + str(solutionK1_largest_error[6]))
print("incumbent solution with largest error rule is: " + str(solutionK1_largest_error[8]))
print("------------------------")
print("for K2 many breakpoints:")
print("------------------------")
'''
print("Solution Time with breakpoint rule is: " + str(solutionK2_breakpoint[0]))
print("node count with breakpoint rule is: " + str(solutionK2_breakpoint[5]))
print("global uppper bound with breakpoint rule is: " + str(solutionK2_breakpoint[6]))
print("incumbent solution with breakpoint rule is: " + str(solutionK2_breakpoint[8]))
print("------------------------")
'''
print("Solution Time with longest edge rule is: " + str(solutionK2_longest_edge[0]))
print("node count with longest edge rule is: " + str(solutionK2_longest_edge[5]))
print("global uppper bound with longest edge rule is: " + str(solutionK2_longest_edge[6]))
print("incumbent solution with longest edge rule is: " + str(solutionK2_longest_edge[8]))
print("------------------------")
print("Solution Time with largest error rule is: " + str(solutionK2_largest_error[0]))
print("node count with largest error rule is: " + str(solutionK2_largest_error[5]))
print("global uppper bound with largest error rule is: " + str(solutionK2_largest_error[6]))
print("incumbent solution with largest error rule is: " + str(solutionK2_largest_error[8]))
print("------------------------")
if (solutionK1_largest_error[6]<solutionK1_longest_edge[6]):
    print("The largest error rule yielded better result for K1.")
if(solutionK1_largest_error[6]==solutionK1_longest_edge[6]):
    print("Both rules yielded an equal result for K1.")
if(solutionK1_largest_error[6]>solutionK1_longest_edge[6]):
    print("The longest edge rule yielded a better result for K1.")
print("The difference between the results is: "+str(abs(solutionK1_largest_error[6]-solutionK1_longest_edge[6])))
print("------------------------")
if (solutionK2_largest_error[6]<solutionK2_longest_edge[6]):
    print("The largest error rule yielded better result for K2.")
if(solutionK2_largest_error[6]==solutionK2_longest_edge[6]):
    print("Both rules yielded an equal result for K2.")
if(solutionK2_largest_error[6]>solutionK2_longest_edge[6]):
    print("The longest edge rule yielded a better result for K2.")
print("The difference between the results is: "+str(abs(solutionK2_largest_error[6]-solutionK2_longest_edge[6])))
#--------------------------------#
# Plot main result for K1 and K2
# many breakpoints
#--------------------------------#
#meshgrid for plot of approximation with K1 many breakpoints
X1,Y1 = np.meshgrid(plf_breakpoints_x1[0],plf_breakpoints_x1[1])
#meshgrid for plot of approximation with K2 many breakpoints
X2,Y2 = np.meshgrid(plf_breakpoints_x2[0],plf_breakpoints_x2[1])
#get functionvalues of approximation with K1 many breakpoints
Z11,Z12 = np.meshgrid(plf_breakpoints_y1[0],plf_breakpoints_y1[1])
Z1 = Z11 + Z12
#get functionvalues of approximation with K2 many breakpoints
Z21,Z22 = np.meshgrid(plf_breakpoints_y2[0],plf_breakpoints_y2[1])
Z2 = Z21 + Z22

#------------------------------------#
# generate the plot
#------------------------------------#
fig = plt.figure()
#first subplot K1 + incumbent solutions of the different branching rules
ax = fig.add_subplot(1,2,1)
ax.tick_params(axis='both',which='major',labelsize=15)
ax.contour(X1,Y1,Z1,25,cmap='gist_gray')
#incumbent solutions
ax.plot(solutionK1_largest_error[8][0],solutionK1_largest_error[8][1],marker='o',color='red',label='largest error rule')
ax.plot(solutionK1_longest_edge[8][0],solutionK1_longest_edge[8][1],marker='o',color='blue',label='longest edge rule')
#ax.plot(solutionK1_breakpoint[8][0],solutionK1_breakpoint[8][1],marker='o',color='green',label='breakpoint rule')
plt.axis('square')
plt.legend(loc = 'lower left',prop={'size':15})
# second subplot envelope + incumbent solution
ax = fig.add_subplot(1,2,2)
ax.tick_params(axis='both',which='major',labelsize=15)
ax.contour(X2,Y2,Z2,25,cmap='gist_gray')
ax.plot(solutionK2_largest_error[8][0],solutionK2_largest_error[8][1],marker='o',color='red',label='largest error rule')
ax.plot(solutionK2_longest_edge[8][0],solutionK2_longest_edge[8][1],marker='o',color='blue',label='longest edge rule')
#ax.plot(solutionK2_breakpoint[8][0],solutionK2_breakpoint[8][1],marker='o',color='green',label='breakpoint rule')
plt.axis('square')
plt.legend(loc = 'lower left',prop={'size':15})
plt.show()
