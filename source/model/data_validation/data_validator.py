from model.data_validation.i_data_validator import IDataValidator
# from i_data_validator import IDataValidator
import re
import doctest


class DataValidator(IDataValidator):
    # DataValidator written by Steven Snelling
    def validate_data(self, dirty_data_arr):
        # where valid person data goes
        clean_people = []

        try:
            for dirty_person in dirty_data_arr:
                # print("dirty person", dirty_person)

                if len(dirty_person) == 7:
                    cleaned_person = []
                    # print("data is correct length")

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

                # print("Cleaned data before filter: ", cleaned_person)

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
    def validate_empid(empid):
        """
        Checks EMPID = [A-Z][0-9]{3}) e.g. B003

        >>> DataValidator.validate_empid("C002")
        True
        """
        if re.compile("^[A-Z][0-9]{3}$").match(empid):
            return True
        else:
            return False

    @staticmethod
    def validate_gender(gender):
        """
        Checks gender = M or F e.g. M or F

        >>> DataValidator.validate_gender("F")
        True
        """
        if re.compile("^[M|F]$").match(gender):
            return True
        else:
            return False

    @staticmethod
    def validate_age(age):
        """
        Checks age = [0-9]{2} e.g. 0 to 99

        >>> DataValidator.validate_age(str(64))
        True
        """
        if re.compile("^[0-9]{2}$").match(age):
            return True
        else:
            return False

    @staticmethod
    def validate_sales(sales):
        """
        Checks Sales = [0-9]{3} e.g. 330

        >>> DataValidator.validate_sales(str(999))
        True
        """
        if re.compile("^[0-9]{3}$").match(sales):
            return True
        else:
            return False

    @staticmethod
    def validate_bmi(bmi):
        """
        Checks BMI = normal|overweight|obesity|underweight case insensitive

        >>> DataValidator.validate_bmi("Overweight")
        True
        """
        if re.compile("^Normal|Overweight|Obesity|Underweight$").match(bmi):
            return True
        else:
            return False

    @staticmethod
    def validate_salary(salary):
        """
        Checks Salary = [0-9]{2,3} e.g. 33 or 330

        >>> DataValidator.validate_salary(str(24))
        True
        """
        if re.compile("^[0-9]{2,3}$").match(salary):
            return True
        else:
            return False

    @staticmethod
    def validate_birthday(birthday):
        """
        Checks birthday = [0-9]{1,2}-[0-9]{1,2}-[0-9]{4} e.g. 2-5-1967

        >>> DataValidator.validate_birthday("2-6-2014")
        True
        """
        if re.compile("^([0-9]{1,2})-([0-9]{1,2})-([0-9]{4})$").match(birthday):
            return True
        else:
            return False


# doctest.testmod(verbose=True)
