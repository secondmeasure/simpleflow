import unittest
import mock

from cdf.features.ganalytics.ghost import (get_sources,
                                           update_ghost_pages,
                                           save_ghost_pages)


class TestGetSources(unittest.TestCase):
    @unittest.skip
    def test_nominal_case(self):
        expected_result = ["organic", "google", "bing", "yahoo", "social",
                           "twitter", "facebook"]
        actual_result = get_sources()
        self.assertSetEqual(set(expected_result), set(actual_result))


class TestUpdateGhostPages(unittest.TestCase):
    def setUp(self):
        #some RawVisitsStreamDef fields are missing,
        #but it should be ok for the function
        self.entry = ["foo", "organic", "bing", None, 5]

    def test_nominal_case(self):
        ghost_pages = {
            "organic": {"foo": 9, "bar": 2},
            "google": {"foo": 5},
            "bing": {"foo": 4}
        }
        update_ghost_pages(ghost_pages, self.entry)

        expected_ghost_pages = {
            "organic": {"foo": 14, "bar": 2},
            "google": {"foo": 5},
            "bing": {"foo": 9}
        }
        self.assertEqual(expected_ghost_pages, ghost_pages)

    def test_missing_medium(self):
        #organic key is missing. This should never happen at runtime
        #since bing is an organic source
        ghost_pages = {
            "bing": {"foo": 4}
        }
        update_ghost_pages(ghost_pages, self.entry)

        expected_ghost_pages = {
            "organic": {"foo": 5},
            "bing": {"foo": 9}
        }
        self.assertEqual(expected_ghost_pages, ghost_pages)

    def test_missing_source(self):
        #there is currently no key for bing
        ghost_pages = {
            "organic": {"foo": 9, "bar": 2},
        }
        update_ghost_pages(ghost_pages, self.entry)

        expected_ghost_pages = {
            "organic": {"foo": 14, "bar": 2},
            "bing": {"foo": 5}
        }
        self.assertEqual(expected_ghost_pages, ghost_pages)


class TestSaveGhostPages(unittest.TestCase):
    @mock.patch('__builtin__.open')
    def test_nominal_case(self, mock_open):
        mock_open.return_value = mock.MagicMock(spec=file)

        source = "organic"
        ghost_pages = {"foo": 9, "bar": 2}
        output_dir = "/tmp/tests"
        save_ghost_pages(source, ghost_pages, output_dir)

        #test that the correct file was open
        mock_open.assert_call_with("/tmp/tests/top_ghost_pages_organic.tsv")

        #test what is written in the file
        file_handle = mock_open.return_value.__enter__.return_value
        self.assertEqual([mock.call('foo\t9\n'),
                          mock.call('bar\t2\n')],
                         file_handle.write.call_args_list)
