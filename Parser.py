from __future__ import print_function
import re
from Instructions import Instructions
from Configurations import Configurations
from Results import Results
from Data import Memory


class ResultFileWriter:
    def __init__(self, filename, instruction_file_parser):
        self.result_file = filename
        self.results = []
        self.instruction_file_parser = instruction_file_parser


class DataFileParser:
    def __init__(self, filename):
        self.data_file = filename
        self.memory = Memory()
        self.base_address = self.memory.get_base_address()

    def parse_config(self, index, line):
        line = line.strip().upper()
        self.memory.add_address_value(self.base_address + index, line)

    def read_memory(self):
        with open(self.data_file, "r") as data_fp:
            for index, line in enumerate(data_fp):
                self.parse_config(index, line)

    def print_memory(self):
        print(self.memory)


class ConfigFileParser:
    def __init__(self, filename):
        self.config_file = filename
        self.configurations = Configurations()

    def parse_config(self, line):
        line = line.strip().upper()
        if "adder".upper() in line:
            tokens = re.split('\s+', line)
            self.configurations.set_fp_adder_count(int(tokens[2].strip().strip(',')))
            self.configurations.set_fp_adder_cycles(int(tokens[3].strip()))
        elif "Multiplier".upper() in line:
            tokens = re.split('\s+', line)
            self.configurations.set_fp_multiplier_count(int(tokens[2].strip().strip(',')))
            self.configurations.set_fp_multiplier_cycles(int(tokens[3].strip()))
        elif "divider".upper() in line:
            tokens = re.split('\s+', line)
            self.configurations.set_fp_divider_count(int(tokens[2].strip().strip(',')))
            self.configurations.set_fp_divider_cycles(int(tokens[3].strip()))
        elif "I-Cache".upper() in line:
            tokens = re.split('\s+', line)
            self.configurations.set_fp_i_cache_block_count(int(tokens[1].strip().strip(',')))
            self.configurations.set_fp_i_cache_block_size(int(tokens[2].strip()))

    def read_config(self):
        with open(self.config_file, "r") as config_fp:
            for line in config_fp:
                self.parse_config(line)

    def print_configurations(self):
        print(self.configurations)



class InstructionFileParser:
    def __init__(self, filename):
        self.instruction_file =  filename
        self.instructions = []

    def parse_instruction(self, line):
        instruction = Instructions()
        instruction.set_text(line.strip())
        line = line.strip().upper()
        tokens = re.split('\s+', line)
        tokens = [token.strip(',') for token in tokens]
        opcode_token = 0
        if ":" in tokens[0]:
            instruction.set_label(tokens[0].strip(':'))
            opcode_token = 1
        instruction.set_opcode(tokens[opcode_token].strip())
        instruction.set_operands(tokens[opcode_token + 1:])
        return instruction

    def read_instructions(self):
        with open(self.instruction_file, "r") as instruction_fp:
            for instruction in instruction_fp:
                self.instructions.append(self.parse_instruction(instruction))

    def print_instructions(self):
        for instruction in self.instructions:
            print(instruction)



