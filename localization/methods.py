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

import numpy as num
import geometry as gx
from scipy.optimize import minimize


def norm(x, y, mode='2D'):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** .5


def sum_error(x, c, r):
    l = len(c)
    e = 0
    for i in range(l):
        e = e + (norm(x, c[i].std()) - r[i]) ** 2
    return e


def lse(cA):
    l = len(cA)
    r = [w.r for w in cA]
    c = [w.c for w in cA]
    S = sum(r)
    W = [(S - w) / ((l - 1) * S) for w in r]
    p0 = gx.point(0, 0, 0)

    for i in range(l):
        p0 = p0 + W[i] * c[i]

    x0 = num.array([p0.x, p0.y])

    res = minimize(sum_error, x0, args=(c, r), method='BFGS')
    ans = res.x

    return gx.point(ans)
