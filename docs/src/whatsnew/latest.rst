.. include:: ../common_links.inc

|iris_version| |build_date| [unreleased]
****************************************

This document explains the changes made to Iris for this release
(:doc:`View all changes <index>`.)


.. dropdown:: :opticon:`report` |iris_version| Release Highlights
   :container: + shadow
   :title: text-primary text-center font-weight-bold
   :body: bg-light
   :animate: fade-in
   :open:

   The highlights for this minor release of Iris include:

   * N/A

   And finally, get in touch with us on :issue:`GitHub<new/choose>` if you have
   any issues or feature requests for improving Iris. Enjoy!


📢 Announcements
================

#. N/A


✨ Features
===========

#. `@schlunma`_ added weighted aggregation over "group coordinates":
   :meth:`~iris.cube.Cube.aggregated_by` now accepts the keyword `weights` if a
   :class:`~iris.analysis.WeightedAggregator` is used. (:issue:`4581`,
   :pull:`4589`)

#. `@wjbenfold`_ added support for ``false_easting`` and ``false_northing`` to
   :class:`~iris.coord_systems.Mercator`. (:issue:`3107`, :pull:`4524`)

#. `@rcomer`_ and `@wjbenfold`_ (reviewer) implemented lazy aggregation for the
   :obj:`iris.analysis.PERCENTILE` aggregator. (:pull:`3901`)

#. `@pp-mo`_ fixed cube arithmetic operation for cubes with meshes.
   (:issue:`4454`, :pull:`4651`)

#. `@wjbenfold`_ added support for CF-compliant treatment of
   ``standard_parallel`` and ``scale_factor_at_projection_origin`` to
   :class:`~iris.coord_systems.Mercator`. (:issue:`3844`, :pull:`4609`)

#. `@wjbenfold`_ added support datums associated with coordinate systems (e.g.
   :class:`~iris.coord_systems.GeogCS` other subclasses of
   :class:`~iris.coord_systems.CoordSystem`). Loading of datum information from
   a netCDF file only happens when the :obj:`iris.FUTURE.datum_support` flag is
   set. (:issue:`4619`, :pull:`4704`)

#. `@wjbenfold`_ and `@stephenworsley`_ (reviewer) added a maximum run length
   aggregator (:class:`~iris.analysis.MAX_RUN`). (:pull:`4676`)

#. `@wjbenfold`_ and `@rcomer`_ (reviewer) added a ``climatological`` keyword to
   :meth:`~iris.cube.Cube.aggregated_by` that causes the climatological flag to
   be set and the point for each cell to equal its first bound, thereby
   preserving the time of year. (:issue:`1422`, :issue:`4098`, :issue:`4665`,
   :pull:`4723`)

#. `@wjbenfold`_ and `@pp-mo`_ (reviewer) implemented the
   :class:`~iris.coord_systems.PolarStereographic` CRS. (:issue:`4770`,
   :pull:`4773`)

#. `@rcomer`_ and `@wjbenfold`_ (reviewer) enabled passing of the
   :func:`numpy.percentile` keywords through the :obj:`~iris.analysis.PERCENTILE`
   aggregator. (:pull:`4791`)

#. `@wjbenfold`_ and `@bjlittle`_ (reviewer) implemented
   :func:`iris.plot.fill_between` and :func:`iris.quickplot.fill_between`.
   (:issue:`3493`, :pull:`4647`)


🐛 Bugs Fixed
=============

#. `@rcomer`_ reverted part of the change from :pull:`3906` so that
   :func:`iris.plot.plot` no longer defaults to placing a "Y" coordinate (e.g.
   latitude) on the y-axis of the plot. (:issue:`4493`, :pull:`4601`)

#. `@rcomer`_ enabled passing of scalar objects to :func:`~iris.plot.plot` and
   :func:`~iris.plot.scatter`. (:pull:`4616`)

#. `@rcomer`_ fixed :meth:`~iris.cube.Cube.aggregated_by` with `mdtol` for 1D
   cubes where an aggregated section is entirely masked, reported at
   :issue:`3190`.  (:pull:`4246`)

#. `@rcomer`_ ensured that a :class:`matplotlib.axes.Axes`'s position is preserved
   when Iris replaces it with a :class:`cartopy.mpl.geoaxes.GeoAxes`, fixing
   :issue:`1157`.  (:pull:`4273`)

#. `@rcomer`_ fixed :meth:`~iris.coords.Coord.nearest_neighbour_index` for edge
   cases where the requested point is float and the coordinate has integer
   bounds, reported at :issue:`2969`. (:pull:`4245`)

#. `@rcomer`_ modified bounds setting on :obj:`~iris.coords.DimCoord` instances
   so that the order of the cell bounds is automatically reversed
   to match the coordinate's direction if necessary.  This is consistent with
   the `Bounds for 1-D coordinate variables` subsection of the `Cell Boundaries`_
   section of the CF Conventions and ensures that contiguity is preserved if a
   coordinate's direction is reversed. (:issue:`3249`, :issue:`423`,
   :issue:`4078`, :issue:`3756`, :pull:`4466`)

#. `@wjbenfold`_ and `@evertrol`_ prevented an ``AttributeError`` being logged
   to ``stderr`` when a :class:`~iris.fileformats.cf.CFReader` that fails to
   initialise is garbage collected. (:issue:`3312`, :pull:`4646`)

#. `@stephenworsley`_ aligned the behaviour of :obj:`~iris.coords.Cell` equality
   to match :obj:`~iris.coords.Coord` equality with respect to NaN values.
   Two NaN valued Cells are now considered equal. This fixes :issue:`4681` and
   causes NaN valued scalar coordinates to be able to merge be preserved during
   cube merging. (:pull:`4701`)

#. `@wjbenfold`_ fixed plotting of circular coordinates to extend kwarg arrays
   as well as the data. (:issue:`466`, :pull:`4649`)

#. `@wjbenfold`_ and `@rcomer`_ (reviewer) corrected the axis on which masking
   is applied when an aggregator adds a trailing dimension. (:pull:`4755`)

#. `@rcomer`_ and  `@pp-mo`_  ensured that all methods to create or modify a
   :class:`iris.cube.CubeList` check that it only contains cubes.  According to
   code comments, this was supposedly already the case, but there were several bugs
   and loopholes. (:issue:`1897`, :pull:`4767`)


💣 Incompatible Changes
=======================

#. `@rcomer`_ and `@bjlittle`_ (reviewer) updated Iris's calendar handling to be
   consistent with ``cf-units`` version 3.1.  In line with the `Calendar`_
   section in version 1.9 of the CF Conventions, we now use "standard" rather
   than the deprecated "gregorian" label for the default calendar.  Units may
   still be instantiated with ``calendar="gregorian"`` but their calendar
   attribute will be silently changed to "standard".  This may cause failures in
   code that explicitly checks the calendar attribute. (:pull:`4847`)


🚀 Performance Enhancements
===========================

#. `@wjbenfold`_ added caching to the calculation of the points array in a
   :class:`~iris.coords.DimCoord` created using
   :meth:`~iris.coords.DimCoord.from_regular`. (:pull:`4698`)

#. `@wjbenfold`_ introduced caching in :func:`_lazy_data._optimum_chunksize` and
   :func:`iris.fileformats.pp_load_rules._epoch_date_hours` to reduce time spent
   repeating calculations. (:pull:`4716`)

#. `@pp-mo`_ made :meth:`~iris.cube.Cube.add_aux_factory` faster.
   (:pull:`4718`)

#. `@wjbenfold`_ and `@rcomer`_ (reviewer) permitted the fast percentile
   aggregation method to be used on masked data when the missing data tolerance
   is set to 0. (:issue:`4735`, :pull:`4755`)

#. `@wjbenfold`_ improved the speed of linear interpolation using
   :meth:`iris.analysis.trajectory.interpolate` (:pull:`4366`)



🔥 Deprecations
===============

#. N/A


🔗 Dependencies
===============

#. `@rcomer`_ introduced the ``nc-time-axis >=1.4`` minimum pin, reflecting that
   we no longer use the deprecated :class:`nc_time_axis.CalendarDateTime`
   when plotting against time coordinates. (:pull:`4584`)

#. `@wjbenfold`_ and `@bjlittle`_ (reviewer) unpinned ``pillow``. (:pull:`4826`)

#. `@rcomer`_ introduced the ``cf-units >=3.1`` minimum pin, reflecting the
   alignment of calendar behaviour in the two packages (see Incompatible Changes).
   (:pull:`4847`)


📚 Documentation
================

#. `@tkknight`_ added a page to show the issues that have been voted for.  See
   :ref:`voted_issues_top`. (:issue:`3307`, :pull:`4617`)

#. `@wjbenfold`_ added a note about fixing proxy URLs in lockfiles generated
   because dependencies have changed. (:pull:`4666`)

#. `@lbdreyer`_ moved most of the User Guide's :class:`iris.Constraint` examples
   from :ref:`loading_iris_cubes` to :ref:`cube_extraction` and added an
   example of constraining on bounded time. (:pull:`4656`)

#. `@tkknight`_ adopted the `PyData Sphinx Theme`_ for the documentation.
   (:discussion:`4344`, :pull:`4661`)

#. `@tkknight`_ updated our developers guidance to show our intent to adopt
   numpydoc strings and fixed some API documentation rendering.
   See :ref:`docstrings`. (:issue:`4657`, :pull:`4689`)

#. `@trexfeathers`_ added a page with examples of converting various mesh
   formats into the Iris Mesh Data Model. (:pull:`4739`)

#. `@rcomer`_ updated the "Load a Time Series of Data From the NEMO Model"
   gallery example. (:pull:`4741`)

#. `@wjbenfold`_ added developer documentation to highlight some of the
   utilities offered by :class:`iris.IrisTest` and how to update CML and other
   output files. (:issue:`4544`, :pull:`4600`)

#. `@trexfeathers`_ and `@abooton`_ modernised the Iris logo to be SVG format.
   (:pull:`3935`)


💼 Internal
===========

#. `@trexfeathers`_ and `@pp-mo`_ finished implementing a mature benchmarking
   infrastructure (see :ref:`contributing.benchmarks`), building on 2 hard
   years of lessons learned 🎉. (:pull:`4477`, :pull:`4562`, :pull:`4571`,
   :pull:`4583`, :pull:`4621`)

#. `@wjbenfold`_ used the aforementioned benchmarking infrastructure to
   introduce deep (large 3rd dimension) loading and realisation benchmarks.
   (:pull:`4654`)

#. `@wjbenfold`_ made :func:`iris.tests.stock.simple_1d` respect the
   ``with_bounds`` argument. (:pull:`4658`)

#. `@bjlittle`_ and `@trexfeathers`_ (reviewer) migrated to GitHub Actions
   for Continuous-Integration. (:pull:`4503`)

#. `@pp-mo`_ made tests run certain linux executables from the Python env,
   specifically ncdump and ncgen.  These could otherwise fail when run in IDEs
   such as PyCharm and Eclipse, which don't automatically include the Python env
   bin in the system PATH.
   (:pull:`4794`)

#. `@trexfeathers`_ and `@pp-mo`_ improved generation of stock NetCDF files.
   (:pull:`4827`, :pull:`4836`)

#. `@rcomer`_ removed some now redundant testing methods. (:pull:`4838`)

#. `@bjlittle`_ and `@jamesp`_ (reviewer) and `@lbdreyer`_ (reviewer) extended
   the GitHub Continuous-Integration to cover testing on ``py38``, ``py39``,
   and ``py310``. (:pull:`4840` and :pull:`4852`)

#. `@bjlittle`_ and `@trexfeathers`_ (reviewer) adopted `setuptools-scm`_ for
   automated ``iris`` package versioning. (:pull:`4841`)


.. comment
    Whatsnew author names (@github name) in alphabetical order. Note that,
    core dev names are automatically included by the common_links.inc:

.. _@evertrol: https://github.com/evertrol


.. comment
    Whatsnew resources in alphabetical order:

.. _Calendar: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.9/cf-conventions.html#calendar
.. _Cell Boundaries: https://cfconventions.org/Data/cf-conventions/cf-conventions-1.9/cf-conventions.html#cell-boundaries
.. _PyData Sphinx Theme: https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html
.. _setuptools-scm: https://github.com/pypa/setuptools_scm