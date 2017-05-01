from __future__ import  print_function
from collections import defaultdict


class Label:

    label_instruction_mapping = defaultdict(int)

    @classmethod
    def add_label(cls, label, instruction_number):
        cls.label_instruction_mapping[label] = instruction_number

    @classmethod
    def get_label(cls, label):
        return cls.label_instruction_mapping[label]