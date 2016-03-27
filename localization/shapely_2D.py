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

import geometry as gx
from shapely.geometry import Polygon,Point,MultiPolygon

""" 2D shapely polygon models for circles"""

def polygonize(c,d):
	l=len(c)
	P=[Point(0, 0).buffer(1.0)]*l
	for i in range(l):
		pc=c[i]
		r=d[i]
		P[i]=Point(pc.x, pc.y).buffer(r)
	return P
