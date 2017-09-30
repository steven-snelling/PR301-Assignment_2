# from model.data_validation.i_data_validator import IDataValidator
from i_data_validator import IDataValidator
import re


# Written by Steven Snelling
class DataValidator(IDataValidator):

    def validate_data(self, dirty_data_arr):
        clean_people = []
        patterns = {
                     "empid" : "^[A-Z][0-9]{3}$",
                     "gender" : "^[M|F]$",
                     "age" : "^[0-9]{2}$",
                     "sales" : "^[0-9]{3}$"
                   }

        try:
            for dirty_person in dirty_data_arr:

                if len(dirty_person) == 7:
                    cleaned_person = []

                    if self.__test_data(str(dirty_person[0]), patterns["empid"]):
                        print("Valid empid: " + str(dirty_person[0]))
                        cleaned_person.append(str(dirty_person[0]))

                    if self.__test_data(str(dirty_person[1]), patterns["gender"]):
                        print("Valid gender: " + str(dirty_person[1]))
                        cleaned_person.append(str(dirty_person[1]))

                    if self.__test_data(str(dirty_person[2]), patterns["age"]):
                        print("Valid age: " + str(dirty_person[2]))
                        cleaned_person.append(str(dirty_person[2]))

                    if self.__test_data(str(dirty_person[3]), patterns["sales"]):
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
