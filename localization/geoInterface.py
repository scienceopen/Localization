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
