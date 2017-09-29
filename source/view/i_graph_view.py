# Written By Thomas
#
# This defines the abstract methods for the View.
#
# If any of these methods are called without their
# implementation being defined in
# a child class, the NotImplemented error will be thrown.
# This results in the system
# closing however.
#
#


class IGraphView(object):
    def sales_by_gender_graph(self, data_arr):
        raise NotImplementedError("An abstract method has not been overriden")

    def employees_by_gender_graph(self, data_arr):
        raise NotImplementedError("An abstract method has not been overriden")

    def age_verse_salary_graph(self, data_arr):
        raise NotImplementedError("An abstract method has not been overriden")

    def bmi_pie_graph(self, data_arr):
        raise NotImplementedError("An abstract method has not been overriden")

    def manual_person_flow(self):
        raise NotImplementedError("An abstract method has not been overriden")

    def show(self, show_string):
        raise NotImplementedError("An abstract method has not been overriden")
