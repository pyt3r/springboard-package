import unittest
import os
import springboard
from springboard.infra.init import dumpPackageData
from springboard.infra.init import get_version
from springboard.util.log import logger


class TestCase(unittest.TestCase):

    def test_package_data(self):
        package = springboard
        package_data = dumpPackageData(package.__file__)
        basedir = os.path.dirname(package.__file__)
        for fn in package_data[package.__name__]:
            if '*' not in fn:
                filepath = os.path.join(basedir, fn)
                logger.debug(filepath)
                assert os.path.exists(filepath)
            else:
                logger.debug(fn)

    def test_get_version(self):
        assert springboard.__version__ == get_version(springboard.__file__)
