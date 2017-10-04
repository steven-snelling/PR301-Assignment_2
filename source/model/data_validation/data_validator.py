# from model.data_validation.i_data_validator import IDataValidator
from i_data_validator import IDataValidator
import re


# Written by Steven Snelling
class DataValidator(IDataValidator):

    def validate_data(self, dirty_data_arr):
        clean_people = []
        patterns = [
                    "^[A-Z][0-9]{3}$", "^[M|F]$",
                    "^[0-9]{2}$", "^[0-9]{3}$",
                    "^Normal|Overweight|Obesity|Underweight$",
                    "^[0-9]{2,3}$",
                    "^([0-9]{1,2})-([0-9]{1,2})-([0-9]{4})$"
        ]

        try:
            for dirty_person in dirty_data_arr:

                if len(dirty_person) == 7:
                    cleaned_person = []

                    if self.__test_data(str(dirty_person[0]), patterns[0]):
                        print("Valid empid: " + str(dirty_person[0]))
                        cleaned_person.append(str(dirty_person[0]))

                    if self.__test_data(str(dirty_person[1]), patterns[1]):
                        print("Valid gender: " + str(dirty_person[1]))
                        cleaned_person.append(str(dirty_person[1]))

                    if self.__test_data(str(dirty_person[2]), patterns[2]):
                        print("Valid age: " + str(dirty_person[2]))
                        cleaned_person.append(str(dirty_person[2]))

                    if self.__test_data(str(dirty_person[3]), patterns[3]):
                        print("Valid Sales: " + str(dirty_person[3]))
                        cleaned_person.append(str(dirty_person[3]))

                    if self.__test_data(str(dirty_person[4]), patterns[4]):
                        print("Valid BMI: " + str(dirty_person[4]))
                        cleaned_person.append(str(dirty_person[4]))

                    if self.__test_data(str(dirty_person[5]), patterns[5]):
                        print("Valid salary: " + str(dirty_person[5]))
                        cleaned_person.append(str(dirty_person[5]))

                    if self.__test_data(str(dirty_person[6]), patterns[6]):
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
