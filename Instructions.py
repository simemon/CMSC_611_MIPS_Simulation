from __future__ import print_function
import re

class Instructions:
    def __init__(self):
        self.label = None
        self.opcode = None
        self.operands_list = None
        self.text = None
        self.source_register = []
        self.dest_register = []

    def set_text(self, text):
        self.text = text

    def set_opcode(self, opcode):
        self.opcode = opcode

    def set_label(self, label):
        self.label = label

    def set_operands(self, operands_list):
        self.operands_list = operands_list
        self.set_source_register()
        self.set_dest_register()

    def set_source_register(self):
        # WITHOUT CONSIDERING SD INSTRUCTION
        regex = re.compile("[0-9]+\(([a-zA-Z\d]+)\)")
        for operands in self.operands_list[1:]:
            if not operands.isdigit():
                if "(" in operands:
                    self.source_register.append(regex.search(operands).groups()[0])
                else:
                    self.source_register.append(operands)

    def set_dest_register(self):
        # WITHOUT CONSIDERING SD INSTRUCTION
        self.dest_register.append(self.operands_list[0])

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