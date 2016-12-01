============
Localization
============

::Original author:: kamal.shadi85@gmail.com
::Revision author:: me@etoccalino.com   github.com/scienceopen

Localization package provides tools for multilateration and triangulation in a 2D surface.
Long distances are affected by the earth modeled as an ideal sphere having radius of 6378.1 kilometers.

.. contents::


Typical usage
=============
see `ExampleEllipsoid.py <ExampleEllipsoid.py>`_::

  import localization
  project = localization.Project(mode=<mode>)

where <mode> is one of::

    2D
    3D

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
============
::

    python setup.py develop


Running the tests
=================

To run the (black box, and very brief) test suite, use::

  python tests.py
