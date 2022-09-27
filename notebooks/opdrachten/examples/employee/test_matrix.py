import unittest
from matrix_jeroen import Matrix

class TestMatrix(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    matrix1 = Matrix(vectorList1)
    matrix2 = Matrix(vectorList2)

    def test_multiply(self):
        print('test_matrix')
        self.assertEqual(self.vectorColumn1, [[1, 1, 1], [1, 1, 1]])
        self.assertEqual(self.vectorColumn2, [[1, 2, 3], [4, 5, 6]])
        # self.assertEqual(self.employee2.fullname, 'Anton Diepenhorst')

    # def test_annualSalary(self):
    #     print('test_apply_raise')
    #     self.employee1.annualSalary
    #     self.employee2.annualSalary

if __name__ == '__main__':
    unittest.main()
