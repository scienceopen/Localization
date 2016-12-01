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

from .geometry import point, circle
from .methods import lse
import logging


class Anchor:
    def __init__(self, ID, loc):
        self.loc = loc
        self.ID = str(ID)

    def __str__(self):
        return 'Anchor '+self.ID+' @ '+self.loc.__str__()


class Target:
    def __init__(self, ID):
        self.loc = None
        self.ID = str(ID)
        self.measures = []

    def __str__(self):
        if self.loc is None:
            return 'Target '+self.ID
        else:
            return 'Target '+self.ID+' @ Real Location:'+self.loc.__str__()

    def add_measure(self, a, d):
        self.measures.append((a, d))


class Project:

    def __init__(self, detail=False):
        self.detail = detail
        self.AnchorDic = {}
        self.TargetDic = {}
        self.nt = 0
        self.log = logging.getLogger(__file__)

    def add_anchor(self, ID, loc):
        try:
            self.AnchorDic[ID]
            self.log.error(str(ID)+':Anchor with same ID already exists')
            return
        except KeyError:
            a = Anchor(ID, point(loc))
            self.AnchorDic[ID] = a
        return a

    def add_target(self, ID=None):
        try:
            self.TargetDic[ID]
            self.log.error('Target with same ID already exists')
            return
        except:
            self.nt = self.nt+1
            if ID:
                pass
            else:
                ID = 't'+str(self.nt)
            t = Target(ID)
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
                cA.append(circle(c, d))

            # Solve using LSE
            tar.loc = lse(cA)
