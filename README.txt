============
Localization
============

Localization package provides tools for multilateration and triangulation
in '2D','3D' and on earth surface.
The current model of the earth, supported by the package, is called 'Earth1'.
Earth1 models the earth as an ideal sphere having radius of 6378.1 kilometers. Typical usage of the package is::

    import localization as lx

To initilaize new localization Project use::

    project = lx.Project(mode=<mode>,solver=<solver>)

Currently three modes are supported:

  * "2D"
  * "3D"
  * "Earth1"

Also three solvers can be utilized:

  * "LSE" for least square error
  * "LSE_GC" for least square error with geometric constraints. Geometric constraints force the solutions to be in the intersection areas of all multilateration circles.
  * "CCA" for centroid method, i.e., the solution will be the centroid of the intersection area. If no common intersection area exist, the area with maximum overlap is used.

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


Contact
-------

Original author: kamal.shadi85@gmail.com
Revision author: me@etoccalino.com
