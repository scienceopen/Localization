#!/usr/bin/env python
"""
2-D example
"""
import localization
from math import hypot
from sys import stderr

OBSNAME = ('radar1','radar2','radar3')
OBSLOC = ((1,  1),
          (-1,-1),
          (-1, 1))

TARGETLOC = (0.2389,0.82)

ranges = [hypot((x-TARGETLOC[0]),y-TARGETLOC[1]) for x,y in OBSLOC]

P = localization.Project(mode='2D')
#%% observers
for device, position in zip(OBSNAME,OBSLOC):
    P.add_anchor(device, position)
#%% Add a target
target, target_label = P.add_target()
#%% Add the observations on the target
for n,r in zip(OBSNAME,ranges):
    target.add_measure(n,r)
#%% Run the solver
P.solve()
#%% print result
errormag = abs(hypot(TARGETLOC[0]-target.loc.x,TARGETLOC[1]-target.loc.y))
print('(x,y) = ({},{})'.format(target.loc.x,target.loc.y))
print('error = {:.3e} m'.format(errormag))

if errormag>1e-3:
    print('excessive error',file=stderr)