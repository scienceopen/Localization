============
Localization
============

Localization package provides tools for multilateration and triangulation in a 2D surface. Long distances are affected by the the a model the earth as an ideal sphere having radius of 6378.1 kilometers. Typical usage of the package is::

  import localization
  project = localization.Project(mode=<mode>,solver=<solver>)

To add anchors to the project use::

  project.add_anchor("anchor name", loc)

where name denote user provided label of the anchor and **loc** is the location of the anchor provided in tuple, e.g., (120,60).
To add target use::

  target, label = project.add_target()

**target** is the target object and **label** is the package provided label for the target.

Distance measurements must be added to target object like::

  target.add_measure("anchor name", measured_distance)

Finally running ``project.solve()`` will locate all targets. You can access the estimated location of the target by ``target.loc``.
``target.loc`` is a point object. Point object B has "x","y","z" coordinates available by B.x, B.y, B.z respectively::

  print("target found at:", round(target.loc.x, 2), round(target.loc.y, 2))


Installation
------------

*Localization* depends on *numpy*, *scipy* (which requires *lapack* with dev headers, a fortran compiler (e.g. *gfortran*)), *shapely* (which requires *libgeos* with its dev headers).

Provided you have already installed:

  * the lapack package with header files
  * the libgeos with its header files
  * a fortran compiler

then to install Localization use::

  pip install .


Running the tests
-----------------

To run the (black box, and very brief) test suite, use::

  python setup.py test


Contact
-------

* Original author: kamal.shadi85@gmail.com
* Revision author: me@etoccalino.com
