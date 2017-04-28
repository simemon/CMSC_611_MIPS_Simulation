from collections import OrderedDict
class Memory:
    def __init__(self):
        self.base_address = 0x100
        self.address_value = OrderedDict()

    def set_base_address(self, base_address):
        self.base_address = base_address

    def get_base_address(self):
        return self.base_address

    def add_address_value(self, address, value):
        self.address_value[address] = value

    def __str__(self):
        return_string = ""
        return_string += "Base Address: {0}\n".format(self.base_address)
        return_string += "Address Value Mapping:\n"
        for address, value in self.address_value.items():
            return_string += "{1} at {0}\n".format(address, value)
        return return_string

    def __repr__(self):
        return self.__str__()


