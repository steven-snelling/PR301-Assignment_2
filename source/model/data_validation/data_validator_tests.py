import unittest
from data_validator import *


class DataValidatorTests(unittest.TestCase):
    # DataValidatorTests structure first 7 test cases done by Steven Snelling
    @classmethod
    def setUpClass(cls):
        cls.dataValidator = DataValidator()

    def setUp(self):
        # be executed before each test
        print("set up")
        self.data = [['A001', 'F', '23', '456', 'Normal', '23', '30-05-1994'],
                     ['C234', 'M', '5', '676', 'Overweight', '300', '1-12-1977'],
                     ['C4', 'Male', 'nine', '66,8', 'heavy', '3,00', '1-12-19']]

        self.data_2 = [['H001', 'M', '16', '200', 'Normal', '230', '30-05-1999']]

        self.data_3 = [['', '', '', '', '', '', '']]

        self.data_4 = [['H001', 'Male', 'eight', '2oo', 'Normal', '230', '30-05-1999']]

        self.data_5 = [['@001', '~', '!', '&&&', '^', '$', '*-05-*']]

    def tearDown(self):
        # be executed after each test case
        print("teardown")

    def test_data_validator_01(self):
        # good day for testing validator
        result = [['H001', 'M', '16', '200', 'Normal', '230', '30-05-1999']]
        self.assertEqual(self.dataValidator.validate_data(self.data_2), result, "That is not a valid data array")

    def test_data_validator_02(self):
        # bad day for testing validator no data
        result = []
        self.assertEqual(self.dataValidator.validate_data(self.data_3), result, "That is not a valid data array")

    def test_data_validator_03(self):
        # bad day for testing validator some data
        result = []
        self.assertEqual(self.dataValidator.validate_data(self.data_4), result, "That is not a valid data array")

    def test_data_validator_04(self):
        # bad day for testing validator can it handle special characters
        result = []
        self.assertEqual(self.dataValidator.validate_data(self.data_5), result, "That is not a valid data array")

    def test_person_age_01(self):
        # good day test for person 1
        age = self.data[0][2]
        self.assertTrue(self.dataValidator.validate_age(age), "That is not a valid age input")

    def test_person_age_02(self):
        # good day test for person 2
        age = self.data[1][2]
        self.assertFalse(self.dataValidator.validate_age(age), "That is not a valid age input")

    def test_person_age_03(self):
        # bad day test for person 3 bad data is rejected
        age = self.data[2][2]
        self.assertFalse(self.dataValidator.validate_age(age), "That is not a valid age input")

    #
    #
    # vaishali
    # Testing valid employeeID input
    def test_person_empid_01(self):
        empid = self.data[0][0]
        self.assertTrue(self.dataValidator.validate_empid(empid), "This is a valid EmployeeID input")

    def test_person_empid_02(self):
        empid = self.data[1][0]
        self.assertTrue(self.dataValidator.validate_empid(empid), "This is a valid EmployeeID input")

    def test_person_empid_03(self):
        empid = self.data[2][0]
        self.assertFalse(self.dataValidator.validate_empid(empid), "This is  NOT a valid EmployeeID input")

    # Testing valid gender input
    def test_person_gender_01(self):
        gender = self.data[0][1]
        self.assertTrue(self.dataValidator.validate_gender(gender), "This is a valid Gender input")

    def test_person_gender_02(self):
        gender = self.data[1][1]
        self.assertTrue(self.dataValidator.validate_gender(gender), "This is a valid Gender input")

    def test_person_gender_03(self):
        gender = self.data[2][2]
        self.assertFalse(self.dataValidator.validate_gender(gender), "This is NOT a valid Gender input")

    # Testing valid sales
    def test_person_sales_01(self):
        sales = self.data[0][3]
        self.assertTrue(self.dataValidator.validate_sales(sales), "This is a valid Sales input")

    def test_person_sales_02(self):
        sales = self.data[1][3]
        self.assertTrue(self.dataValidator.validate_sales(sales), "This is a valid Sales input")

    def test_person_sales_03(self):
        sales = self.data[2][3]
        self.assertFalse(self.dataValidator.validate_sales(sales), "This is NOT a valid Sales input")

    # Testing valid BMI input
    def test_person_bmi_01(self):
        bmi = self.data[0][4]
        self.assertTrue(self.dataValidator.validate_bmi(bmi), "This is a valid BMI input")

    def test_person_bmi_02(self):
        bmi = self.data[1][4]
        self.assertTrue(self.dataValidator.validate_bmi(bmi), "This is a valid BMI input")

    def test_person_bmi_03(self):
        bmi = self.data[2][4]
        self.assertFalse(self.dataValidator.validate_bmi(bmi), "This is NOT a valid BMI input")

    # Testing valid Salary input
    def test_person_salary_01(self):
        salary = self.data[0][5]
        self.assertTrue(self.dataValidator.validate_salary(salary), "This is a valid Salary input")

    def test_person_salary_02(self):
        salary = self.data[1][5]
        self.assertTrue(self.dataValidator.validate_salary(salary), "This is a valid Salary input")

    def test_person_salary_03(self):
        salary = self.data[2][5]
        self.assertFalse(self.dataValidator.validate_salary(salary), "This is NOT a valid Salary input")

    # Testing valid Birthdate input
    def test_person_birthday_01(self):
        birthday = self.data[0][6]
        self.assertTrue(self.dataValidator.validate_birthday(birthday), "This is a valid Birthday input")

    def test_person_birthday_02(self):
        birthday = self.data[1][6]
        self.assertTrue(self.dataValidator.validate_birthday(birthday), "This is a valid Birthday input")

    def test_person_birthday_03(self):
        birthday = self.data[2][6]
        self.assertFalse(self.dataValidator.validate_birthday(birthday), "This is NOT a valid Birthday input")

if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()
