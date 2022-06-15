import unittest


class TestSampleClass(unittest.TestCase):

    def test_should_fail(self):
        self.fail('Test failing 5')
        

if __name__=="__main__":
    unittest.main()
