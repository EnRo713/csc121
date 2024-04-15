import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_give_default_raise(self):
        employee = Employee("John", "Doe", 50000)
        employee.give_raise()
        self.assertEqual(employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        employee = Employee("Jane", "Smith", 60000)
        employee.give_raise(10000)
        self.assertEqual(employee.annual_salary, 70000)

if __name__ == '__main__':
    unittest.main()
