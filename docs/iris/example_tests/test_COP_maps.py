# (C) British Crown Copyright 2010 - 2012, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.


# Import Iris tests first so that some things can be initialised before importing anything else.
import iris.tests as tests

import unittest

import extest_util

with extest_util.add_examples_to_path():
    import COP_maps


class TestCOPMaps(tests.GraphicsTest):
    """Test the COP_maps example code."""
    def test_cop_maps(self):
        with extest_util.show_replaced_by_check_graphic(self, tol=0):
            COP_maps.main()


if __name__ == '__main__':
    tests.main()
