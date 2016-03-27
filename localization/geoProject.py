# Copyright 2016 Elvio Toccalino, Kamal Shadi

# This file is part of the Localization package.
#
# Localization is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Localization is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# Localization.  If not, see <http://www.gnu.org/licenses/>.

import geoInterface as gx
import geometry as gm
import methods as mx


class Project:

    def __init__(self, mode='2D', solver='LSE', detail=False):
        self.mode = mode
        self.solver = solver
        self.detail = detail
        self.AnchorDic = {}
        self.TargetDic = {}
        self.nt = 0

    def set_mode(self, mode):
        self.mode = mode

    def set_solver(self, sol):
        self.solver = sol

    def add_anchor(self, ID, loc):
        try:
            self.AnchorDic[ID]
            print str(ID)+':Anchor with same ID already exists'
            return
        except KeyError:
            a = gx.Anchor(ID, gm.point(loc))
            self.AnchorDic[ID] = a
        return a

    def add_target(self, ID=None):
        try:
            self.TargetDic[ID]
            print 'Target with same ID already exists'
            return
        except:
            self.nt = self.nt+1
            if ID:
                pass
            else:
                ID = 't'+str(self.nt)
            t = gx.Target(ID)
            self.TargetDic[ID] = t
        return (t, ID)

    def solve(self, **kwargs):
        for tID in self.TargetDic.keys():
            tar = self.TargetDic[tID]
            cA = []
            for tup in tar.measures:
                landmark = tup[0]
                c = self.AnchorDic[landmark].loc
                d = tup[1]
                cA.append(gm.circle(c, d))
            if self.solver == 'LSE':
                tar.loc = mx.lse(cA, mode=self.mode, cons=False)
            elif self.solver == 'LSE_GC':
                try:
                    tar.loc = mx.lse(cA, mode=self.mode, cons=True)
                except mx.cornerCases as cc:
                    if cc.tag == 'Disjoint':
                        print tar.ID+' could not be localized by LSE_GC'
                    else:
                        print 'Unknown Error in localizing '+tar.ID
            elif self.solver == 'CCA':
                if not self.detail:
                    tar.loc, n = mx.CCA(cA, mode=self.mode, detail=False)
                    return n
                else:
                    tar.loc, n, P, iP = mx.CCA(cA, mode=self.mode, detail=True)
                    return (n, P, iP)
