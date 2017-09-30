# from model.data_validation.i_data_validator import IDataValidator
from i_data_validator import IDataValidator
import re


class DataValidator(IDataValidator):
    # Written by Steven Snelling
    def validate_data(self, dirty_data_arr):
        clean_people = []

        try:
            for dirty_person in dirty_data_arr:

                if len(dirty_person) == 7:
                    cleaned_person = []

                    if self.validate_empid(str(dirty_person[0])):
                        print("Valid empid: " + str(dirty_person[0]))
                        cleaned_person.append(str(dirty_person[0]))

                    if self.validate_gender(str(dirty_person[1])):
                        print("Valid gender: " + str(dirty_person[1]))
                        cleaned_person.append(str(dirty_person[1]))

                    if self.validate_age(str(dirty_person[2])):
                        print("Valid age: " + str(dirty_person[2]))
                        cleaned_person.append(str(dirty_person[2]))

                    if self.validate_sales(str(dirty_person[3])):
                        print("Valid Sales: " + str(dirty_person[3]))
                        cleaned_person.append(str(dirty_person[3]))

                    if self.validate_bmi(str(dirty_person[4])):
                        print("Valid BMI: " + str(dirty_person[4]))
                        cleaned_person.append(str(dirty_person[4]))

                    if self.validate_salary(str(dirty_person[5])):
                        print("Valid salary: " + str(dirty_person[5]))
                        cleaned_person.append(str(dirty_person[5]))

                    if self.validate_birthday(str(dirty_person[6])):
                        print("Valid birthday: " + str(dirty_person[6]))
                        cleaned_person.append(str(dirty_person[6]))
                else:
                    return "Not enough feilds: " + str(len(dirty_person))

                filter(None, cleaned_person)

                print("Cleaned person after filter: ", cleaned_person)

                if len(cleaned_person) == 7:
                    clean_people.append(cleaned_person)

        except TypeError:
            print(TypeError)
            print("You have submitted the wrong data type")

        print("Cleaned people after filter: ", clean_people)

        return clean_people

    @staticmethod
    def __test_data(data, pattern):
        if re.compile(pattern).match(data):
            return True
        else:
            return False

    @staticmethod
    def validate_empid(empid):
        if re.compile("^[A-Z][0-9]{3}$").match(empid):
            return True
        else:
            return False

    @staticmethod
    def validate_gender(gender):
        if re.compile("^[M|F]$").match(gender):
            return True
        else:
            return False

    @staticmethod
    def validate_age(age):
        if re.compile("^[0-9]{2}$").match(age):
            return True
        else:
            return False

    @staticmethod
    def validate_sales(sales):
        if re.compile("^[0-9]{3}$").match(sales):
            return True
        else:
            return False

    @staticmethod
    def validate_bmi(bmi):
        if re.compile("^Normal|Overweight|Obesity|Underweight$").match(bmi):
            return True
        else:
            return False

    @staticmethod
    def validate_salary(salary):
        if re.compile("^[0-9]{2,3}$").match(salary):
            return True
        else:
            return False

    @staticmethod
    def validate_birthday(birthday):
        if re.compile("^([0-9]{1,2})-([0-9]{1,2})-([0-9]{4})$").match(birthday):
            return True
        else:
            return False
