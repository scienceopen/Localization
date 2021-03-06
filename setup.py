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
from __future__ import print_function
from sys import stderr
from subprocess import call
from setuptools import setup

try:
    call(['conda','install','--file','requirements.txt'])
except Exception:
    print('install packages in requirements.txt',file=stderr)


setup(
    name = 'Localization',
    version = '0.2.1',

    author = 'Elvio Toccalino',
    author_email = 'me@etoccalino.com',

    packages = ['localization'],
    install_requires = [],
    test_suite = 'tests',

    url = 'https://github.com/kamalshadi/Localization',
    license = 'LICENSE.txt',

    description = 'Multilateration and triangulation.',
    long_description = open('README.rst').read(),
)
