
"""
Example for Algorithm 1 in the paper of Hübner et al
----------------------------
Author: Sina Anheyer
Year: 2025
Python Version: 3.9.7
----------------------------
implementation in sbb_functions of Algorithm 1 only applies to continuous PLF
this program implements the two functions getEnvelope and getPLFvalue from
sbb_functions such that the input of non continous functions is allowed
----------------------------
functions:
----------------------------
getEnvelope
- this function implements Algorithm 1 from the paper

getPLFvalue
-this function calculates the PLF value defined by the lists breakpoints
 and values at a given point x
"""
import bisect 
import numpy as np
import matplotlib.pyplot as plt

def getEnvelope(B,V):
    '''
    this function calculates a convex envelope for a (possibly non continuous) PLF
    ------------
    input:

    B : list (of breakpoints)
    V : list of lists elements have the shape [y-,y,y+] (list of function values)

    ------------
    output:

    Bnew : list (breakpoints of envelope)
    Vnew : list (functionvalues of envelope)
    '''
    #initialising working list Vlo
    Vlow  = []
    #compute continuous (possibly non convex) underestimator
    for i in range(len(V)):
        Vlow.append(min(V[i]))

    #compute the convex envelope of the continuous function given by B and Vlow

    #initialise Bnew and Vnew
    Bnew = [B[0]]
    Vnew = [Vlow[0]]

    #begin for-loop
    for i in range(1,len(B)):
        while (len(Bnew) >= 2 and 
               ((Vlow[i] - Vnew[-1]) / (B[i] - Bnew[-1]) < 
                (Vnew[-1] - Vnew[-2]) / (Bnew[-1] - Bnew[-2]))):
            Bnew.pop()
            Vnew.pop()
 
        Bnew.append(B[i])
        Vnew.append(Vlow[i])

    return Bnew, Vnew

def getPLFvalue(B,V,x):
    '''
    This function calculates the value F(x)
    for a (possibly non continuous) PLF defined by its breakpoints and function values
    ------
    input:
    B : list of breakpoints
    V : list of lists elements either have the shape [y] or [y-,y,y+] (list of function values)
    x : float

    -----
    output:
    y : PLF value at x
    '''
    #retrieve position of x in B
    pos = bisect.bisect(B,x)
    if x  == B[pos-1]:
        y = V[pos-1][1]
    else:
        y = ((V[pos][0] - V[pos-1][2]) 
             / (B[pos]-B[pos-1]) 
            ) * (x-B[pos-1]) + V[pos-1][2]
    return y

#-------------------------------------------#
# BEGINN EXAMPLE
#-------------------------------------------#

#Example for non continuous PLF function
B_ex = [1,3,4,6,7,9,11,12,13,14]
V_ex = [[7,7,7],[5.5,1,4],[3,3,3],[2.5,2.5,2.5],[1.5,1,0.5],[1.5,2.5,12],[4,4,4],[6,6,6],[6.5,6.5,6.5],[6,6,6]]

# calculate convex envelope
B_env,V_env = getEnvelope(B_ex,V_ex)

#adapt V_env such that it is a suitable input for getPLFvalue
V_env_lists = []
for i in range(len(V_env)):
    V_env_lists.append([V_env[i],V_env[i],V_env[i]])

# plot both functions - envelope and original function
X = np.linspace(1,13.999,1000)
Y_env=[]
for x in X:
    Y_env.append(getPLFvalue(B_env,V_env_lists,x))

# generate plot
fig = plt.figure()
#first subplot of nonconvex PLF
ax = fig.add_subplot(1,2,1)
ax.tick_params(axis='both',which='major',labelsize=15)
for i in range(1,len(B_ex)):
    X_segment = [B_ex[i-1],B_ex[i]]
    Y_segment = [V_ex[i-1][2],V_ex[i][0]]
    x_point   = B_ex[i]
    y_point1  = V_ex[i][1]
    ax.plot(X_segment,Y_segment,color='red')
    ax.plot(x_point,y_point1,ms=3,color='red',marker='o')
    ax.plot(x_point,V_ex[i][0],ms=3,color='red',marker='o')
    ax.plot(x_point,V_ex[i][2],ms=3,color='red',marker='o')
plt.axis('square')
ax.legend('f',fontsize ="20")

# second subplot envelope 
ax = fig.add_subplot(1,2,2)
ax.tick_params(axis='both',which='major',labelsize=15)
ax.plot(X,Y_env,color='red',label = '$covx_{I}f$')
plt.axis('square')
ax.legend(fontsize ="20")
plt.show()