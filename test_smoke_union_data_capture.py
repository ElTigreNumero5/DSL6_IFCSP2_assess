import unittest  # import the unittest testing framework
import union_data_capture  # import our app's main code module


class SmokeTest(unittest.TestCase):
    def test_ut_good1(self):
        self.assertIsInstance({}, dict)  #  assertion - check an empty dictionary object is a dictionary class

if __name__ == '__main__':
    unittest.main(verbosity=1, exit=True)
    my_app = union_data_capture.UnionCollect()
    my_app.mainloop()
