import unittest
from cdf.features.main.helpers.masks import urlinfos_mask


class TestUrlinfosMask(unittest.TestCase):
    def test_nominal_case(self):
        self.assertItemsEqual(["has_canonical", "gzip"], urlinfos_mask(17))

    def test_empty_result(self):
        self.assertItemsEqual([], urlinfos_mask(0))

    def test_single_attribute(self):
        self.assertItemsEqual(["bad_canonical"], urlinfos_mask(32))

    def test_out_of_range(self):
        self.assertItemsEqual([], urlinfos_mask(128))
        self.assertItemsEqual([], urlinfos_mask(-1))

    def test_unused_value(self):
        self.assertItemsEqual([], urlinfos_mask(2))
