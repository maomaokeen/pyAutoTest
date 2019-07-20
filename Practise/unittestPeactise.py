import unittest
from io import StringIO


class lesson(unittest.TestCase):

    def setUp(self):
        self.f = StringIO()
        print("创建StringIO")

    def tearDown(self):
        s = self.f.getvalue()
        print("读取StringIO：", s)

    def test_case1(self):
        self.f.write("test case 1")
        print("写入test case 1")

    def test_case2(self):
        self.f.write("test case 2")
        print("写入test case 2")


if __name__ == '__main__':
    unittest.main()