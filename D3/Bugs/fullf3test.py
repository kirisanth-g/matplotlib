import unittest
import os
import sys
import six
import matplotlib

class EnvironVarTest(unittest.TestCase):
    def test_no_var(self):
        #linux test
        if sys.platform == 'linux':
            self.assertEqual(matplotlib._get_home(), os.path.expanduser("~"),
            "linux value overridden")
        #windows
        elif sys.platform == "win32":
            self.assertEqual(matplotlib._get_gome(), 
            os.path.expanduser(b"~").decode(sys.getfilesystemencoding()),
            'windows value overridden')
        #unix
        else:
            self.assertEqual(matplotlib._get_home(), os.path.expanduser("~"),
            "unix value overridden")

    def test_with_var_valid_path(self):
        #setting variable in windows
        if sys.platform == "win32":
            os.environ["MATPDIR"] == "C:"
        #setting variable for unix
        else:
            os.environ["MATPDIR"] = "/"

        self.assertEqual(matplotlib._get_home(), os.environ.get('MATPDIR'),
        "MATPDIR was not read")

    def test_with_var_invalid_path(self):
        os.environ["MATPDIR"] = "_________________"

        #linux test
        if sys.platform == 'linux':
            self.assertEqual(matplotlib._get_home(), os.path.expanduser("~"),
            "linux value overridden with invalid path")
        #windows
        elif sys.platform == "win32":
            self.assertEqual(matplotlib._get_gome(), 
            os.path.expanduser(b"~").decode(sys.getfilesystemencoding()),
            "windows value overridden with invalid path")
        #unix
        else:
            self.assertEqual(matplotlib._get_home(), os.path.expanduser("~"),
            "unix value overridden with invalid path")



if __name__ == "__main__":
    unittest.main()
