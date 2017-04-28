from __future__ import print_function
class Instructions:
    def __init__(self):
        self.label = None
        self.opcode = None
        self.operands_list = None

    def set_opcode(self, opcode):
        self.opcode = opcode

    def set_label(self, label):
        self.label = label

    def set_operands(self, operands_list):
        self.operands_list = operands_list

    def __str__(self):
        return_string = ""
        if self.label is not None:
            return_string += "Label: {0}".format(self.label) + ","
        return_string += "Opcode: {0}".format(self.opcode) + ","
        if self.operands_list:
            return_string += "Operands List: {0}".format(self.operands_list)
        return return_string.strip(',')

    def __repr__(self):
        return self.__str__()