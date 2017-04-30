from __future__ import print_function
from collections import defaultdict

class RegisterObject:

    def __init__(self):
        self.last_read = 0
        self.last_write = 0
        self.value = 0

class Register:
    value = defaultdict(RegisterObject)

    def __init__(self):
        pass

    @classmethod
    def print_values(self):
        for register, val in self.value.items():
            print("{1} on {0}".format(register, val.value))

class Floating:
    value = defaultdict(RegisterObject)

    def __init__(self):
        pass

    @classmethod
    def print_values(self):
        print("REGISTER VALUES:")
        for register, val in self.value.items():
            print("{1} on {0}".format(register, val))