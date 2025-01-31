"""
Unit tests for loaders

"""

import neuroml
from neuroml import loaders
import os

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestNeuroMLLoader(unittest.TestCase):
    def test_load_neuroml(self):
        root_dir = os.path.dirname(neuroml.__file__)
        print("root dir is: " + root_dir)
        test_file_path = os.path.join(root_dir, "examples/test_files/Purk2M9s.nml")
        print("test fi le path is: " + test_file_path)

        f = open(test_file_path, "r")
        # print(f.read())
        doc = loaders.NeuroMLLoader.load(test_file_path)
        self.assertEqual(doc.id, "Purk2M9s")
        f.close()
        print("Finished test")

    def test_non_neuroml_file(self):
        """Test an non-NeuroML document."""
        root_dir = os.path.dirname(neuroml.__file__)
        test_file_path = os.path.join(root_dir, "examples/test_files/sbml-example.xml")
        print("test file path is: " + test_file_path)

        try:
            loaders.NeuroMLLoader.load(test_file_path)
        except TypeError:
            print("Exception raised. Test passes.")


if __name__ == "__main__":
    t = TestNeuroMLLoader()
    t.test_load_neuroml()
