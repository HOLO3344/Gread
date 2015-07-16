# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name = None, Id = None):
        self.name = name
        self.Id = Id
        self.English = 0.0
        self.Math = 0.0
    def calc_gread(self):
        return self.English + self.Math

    def print_message(self):
        print "*" * 20
        print "Student Name: %s" % self.name
        print "Id          : %s" % self.Id
        print "Englsh gread: %f" % self.English
        print "Math gread  : %f" % self.Math
        print "Total gread : %f" % self.calc_gread()
        print "*" * 20

ss = Student()

if __name__ == '__main__':

    ss.print_message()
    ss.name = "holo"
    ss.Id = "201322240117"
    ss.English = 79
    ss.Math = 80

    ss.print_message()
