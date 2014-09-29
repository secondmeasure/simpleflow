import unittest

from cdf.features.links.helpers.predicates import is_follow_link

class TestIsFollowLink(unittest.TestCase):
    def test_bitmask(self):
        self.assertTrue(is_follow_link(0, True))
        self.assertTrue(is_follow_link(8, True))
        self.assertFalse(is_follow_link(1, True))
        self.assertFalse(is_follow_link(3, True))

    def test_not_bitmask(self):
        self.assertTrue(is_follow_link(["follow"]))
        self.assertTrue(is_follow_link(["follow"]))
        self.assertFalse(is_follow_link(["foo"]))
        self.assertFalse(is_follow_link([]))