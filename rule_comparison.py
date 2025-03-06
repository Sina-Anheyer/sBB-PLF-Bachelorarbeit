"""
Author: Sina Anheyer
Computational Experiment:
Comparison between the largest error branching rule and the longest edge branching rule
Problem type: non concave knapsack
------------------------------------------------------
The experiments require the following modules from Hübner et.al:
instance_generation.py
gurobi_solver.py
------------------------------------------------------
as well as my own adapted versions of sBB_main.py and sBB_functions.py
that allow for solving via the longest edge rule:
sBB_functions_rules.py
sBB_main_rules.py
"""
import sBB_main_rules as sBB
import sBB_functions_rules as sBBf
import instance_generation as ig
import numpy as np
import random
import matplotlib.pyplot as plt
import io #Necessary for suppressing print
from contextlib import redirect_stdout #Necessary for suppressing print


#----------------------------------
# Parameters
#----------------------------------

#amount of breakpoints:
breakpoints = [10,50,100,500,750]
#amount of random test problems:
test_number = 50
#termination gap:
epsilon = 0.00001
#dimension of the random knapsack problems:
d = 5
#time limit
t = 10


#----------------------------------------------------------
# BEGIN EXPERIMENT
#----------------------------------------------------------

average_solve_times_longest_edge  = []
average_solve_times_largest_error = []
average_node_count_longest_edge   = []
average_node_count_largest_error  = []

for k in range(len(breakpoints)):
    print( "we are at: " + str(k))
#----------------------------------------------------------
# Generate random separable PLF with dimension d
# solve both with longest edge rule and largest error rule
#----------------------------------------------------------

    solve_times_longest_egde = []
    node_count_longest_edge = []

    solve_times_largest_error = []
    node_count_largest_error = []

    for j in range(test_number):
        # randomly select d functions from function catalogue in 
        # instance_generation.py
        list_of_functions = []
        for i in range(d):
            list_of_functions.append(random.randrange(1,20,1))

        # aquire PLF
        [plf_breakpoints_x,plf_breakpoints_y] = ig.getPLFs(d,breakpoints[k],list_of_functions,False)

        #generate random demand parameter for problem
        rhs = ig.getRHS(d,breakpoints[k],"knapsack",plf_breakpoints_x)

        #solve problem with longest egde rule:
        longest_edge = sBB.spatialBB(plf_breakpoints_x,plf_breakpoints_y,d,breakpoints[k],"knapsack",rhs,t,epsilon,"longest edge")
        #solve problem with largest error rule
        largest_error = sBB.spatialBB(plf_breakpoints_x,plf_breakpoints_y,d,breakpoints[k],"knapsack",rhs,t,epsilon,"largest error")

        solve_times_longest_egde.append(longest_edge[0])
        solve_times_largest_error.append(largest_error[0])

        node_count_longest_edge.append(longest_edge[5])
        node_count_largest_error.append(largest_error[5])
    
    average_node_count_longest_edge.append(sum(node_count_longest_edge)/test_number)
    average_node_count_largest_error.append(sum(node_count_largest_error)/test_number)

    average_solve_times_longest_edge.append(sum(solve_times_longest_egde)/test_number)
    average_solve_times_largest_error.append(sum(solve_times_largest_error)/test_number)

#--------------------------------------
# END EXPERIMENT
#--------------------------------------

# OUTPUT
print("avrg. solve time longest edge: " + str(average_solve_times_longest_edge))
print("------------------------------")
print("avrg. solve time largest error: " + str(average_solve_times_largest_error))
print("------------------------------")
print("avrg. node count longest edge: " + str(average_node_count_longest_edge))
print("------------------------------")
print( "avrg. node count largest error: " + str(average_node_count_largest_error))

