from __future__ import print_function

class Configurations:
    def __init__(self):
        self.fp_adder_count = 0
        self.fp_adder_cycles = 0
        self.fp_multiplier_count = 0
        self.fp_multiplier_cycles = 0
        self.fp_divider_count = 0
        self.fp_divider_cycles = 0
        self.i_cache_block_count = 0
        self.i_cache_block_size = 0
        self.arithmetic_count = 1
        self.arithmetic_cycles = 1
        self.data_count = 1
        self.data_cycles = 2
        self.branch_count = 1
        self.branch_cycles = 1
        self.control_count = 1
        self.control_cycles = 1

    def set_fp_adder_count(self, fp_adder_count):
        self.fp_adder_count = fp_adder_count

    def set_fp_adder_cycles(self, fp_adder_cycles):
        self.fp_adder_cycles = fp_adder_cycles

    def set_fp_multiplier_count(self, fp_multiplier_count):
        self.fp_multiplier_count = fp_multiplier_count

    def set_fp_multiplier_cycles(self, fp_multiplier_cycles):
        self.fp_multiplier_cycles = fp_multiplier_cycles

    def set_fp_divider_count(self, fp_divider_count):
        self.fp_divider_count = fp_divider_count

    def set_fp_divider_cycles(self, fp_divider_cycles):
        self.fp_divider_cycles = fp_divider_cycles

    def set_fp_i_cache_block_count(self, fp_i_cache_block_count):
        self.i_cache_block_count = fp_i_cache_block_count

    def set_fp_i_cache_block_size(self, fp_i_cache_block_size):
        self.i_cache_block_size = fp_i_cache_block_size

    def __str__(self):
        return_string = ""
        return_string += "FP Adder Count: {0}\n".format(self.fp_adder_count)
        return_string += "FP Adder Cycles: {0}\n".format(self.fp_adder_cycles)
        return_string += "FP Multiplier Count: {0}\n".format(self.fp_multiplier_count)
        return_string += "FP Multiplier Cycles: {0}\n".format(self.fp_multiplier_cycles)
        return_string += "FP Divider Count: {0}\n".format(self.fp_divider_count)
        return_string += "FP Divider Cycles: {0}\n".format(self.fp_divider_cycles)
        return_string += "I-Cache Block Count: {0}\n".format(self.i_cache_block_count)
        return_string += "I-Cache Block Size: {0}\n".format(self.i_cache_block_size)
        return return_string.strip(',')

    def __repr__(self):
        return self.__str__()

