import unittest
import os
import sys
import six
import feature3 as f3

class EnvironVarTest(unittest.TestCase):
    def test_no_var(self):
        #linux test
        if sys.platform == 'linux':
            self.assertEqual(f3._get_home(), os.path.expanduser("~"),
            "linux value overridden")
        #windows
        elif sys.platform == "win32":
            self.assertEqual(f3._get_gome(), 
            os.path.expanduser(b"~").decode(sys.getfilesystemencoding()),
            'windows value overridden')
        #unix
        else:
            self.assertEqual(f3._get_home(), os.path.expanduser("~"),
            "unix value overridden")

    def test_with_var(self):
        #setting variable in windows
        if sys.platform == "win32":
            os.environ["MATPDIR"] == "C:"
        #setting variable for unix
        else:
            os.environ["MATPDIR"] = "/"

        self.assertEqual(f3._get_home(), os.environ.get('MATPDIR'),
        "MATPDIR was not read")


if __name__ == "__main__":
    unittest.main()
