from __future__ import print_function


class Instruction_Data:
    count = 0
    min_value = 0
    min_index = 0
    execution_cycle = 0

    def __init__(self, count, execution_cycle):
        Instruction_Data.count = count
        Instruction_Data.execution_cycle = execution_cycle
        self.isBusy = False
        self.when_available = 0

    @classmethod
    def set_min_value_index(cls, objects):
        for ind, obj in enumerate(objects):
            if obj.when_available < cls.min_val:
                cls.min_val = obj.when_available
                cls.min_index = ind


class Instruction_Arithmetic:
    count = 0
    min_value = 0
    min_index = 0
    execution_cycle = 0

    def __init__(self, count, execution_cycle):
        Instruction_Data.count = count
        Instruction_Data.execution_cycle = execution_cycle
        self.isBusy = False
        self.when_available = 0

    @classmethod
    def set_min_value_index(cls, objects):
        for ind, obj in enumerate(objects):
            if obj.when_available < cls.min_val:
                cls.min_val = obj.when_available
                cls.min_index = ind


class Instruction_Adder:
    count = 0
    min_value = 0
    min_index = 0
    execution_cycle = 0

    def __init__(self, count, execution_cycle):
        Instruction_Adder.count = count
        Instruction_Adder.execution_cycle = execution_cycle
        self.isBusy = False
        self.when_available = 0

    @classmethod
    def set_min_value_index(cls, objects):
        for ind, obj in enumerate(objects):
            if obj.when_available < cls.min_val:
                cls.min_val = obj.when_available
                cls.min_index = ind


class Instruction_Multiplier:
    count = 0
    min_value = 0
    min_index = 0
    execution_cycle = 0

    def __init__(self, count, execution_cycle):
        Instruction_Multiplier.count = count
        Instruction_Multiplier.execution_cycle = execution_cycle
        self.isBusy = False
        self.when_available = 0

    @classmethod
    def set_min_value_index(cls, objects):
        for ind, obj in enumerate(objects):
            if obj.when_available < cls.min_val:
                cls.min_val = obj.when_available
                cls.min_index = ind


class Instruction_Divider:
    count = 0
    min_value = 0
    min_index = 0
    execution_cycle = 0

    def __init__(self, count, execution_cycle):
        Instruction_Divider.count = count
        Instruction_Divider.execution_cycle = execution_cycle
        self.isBusy = False
        self.when_available = 0

    @classmethod
    def set_min_value_index(cls, objects):
        for ind, obj in enumerate(objects):
            if obj.when_available < cls.min_val:
                cls.min_val = obj.when_available
                cls.min_index = ind


class Instruction_Conditional:
    count = 0
    min_value = 0
    min_index = 0
    execution_cycle = 0

    def __init__(self, count, execution_cycle):
        Instruction_Conditional.count = count
        Instruction_Conditional.execution_cycle = execution_cycle
        self.isBusy = False
        self.when_available = 0


class Instruction_UnConditional:
    count = 0
    min_value = 0
    min_index = 0
    execution_cycle = 0

    def __init__(self, count, execution_cycle):
        Instruction_UnConditional.count = count
        Instruction_UnConditional.execution_cycle = execution_cycle
        self.isBusy = False
        self.when_available = 0


class Instruction_Control:
    count = 0
    min_value = 0
    min_index = 0
    execution_cycle = 0

    def __init__(self, count, execution_cycle):
        Instruction_Control.count = count
        Instruction_Control.execution_cycle = execution_cycle
        self.isBusy = False
        self.when_available = 0

