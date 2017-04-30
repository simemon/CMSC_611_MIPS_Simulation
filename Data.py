from collections import OrderedDict


class Memory:

    def __init__(self):
        self.base_address = 0x100
        self.address_string_value = OrderedDict()
        self.address_actual_value = OrderedDict()

    def set_base_address(self, base_address):
        self.base_address = base_address

    def get_base_address(self):
        return self.base_address

    def add_address_value(self, address, string):
        self.address_string_value[address] = string
        self.address_actual_value[address] = int(string, 2)

    def get_value(self, address):
        return self.address_actual_value[address]

    def set_value(self, address, value):
        self.address_actual_value[address] = value
        self.address_string_value = '{0:032b}'.format(value)

    def __str__(self):
        return_string = ""
        return_string += "Base Address: {0}\n".format(self.base_address)
        return_string += "Address Value Mapping:\n"
        for address, value in self.address_string_value.items():
            return_string += "{1} [{2}] at {0}\n".format(address, value, self.address_actual_value[address])
        return return_string

    def __repr__(self):
        return self.__str__()


