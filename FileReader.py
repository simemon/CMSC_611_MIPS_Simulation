from __future__ import print_function
from Parser import InstructionFileParser, ConfigFileParser, DataFileParser


class argumentReader:

    instr_file_reader = None
    config_file_reader = None
    data_file_reader = None

    @classmethod
    def parse_files(cls, data_file, instruction_file, config_file):
        print("Instruction File Parsing Started")
        cls.instr_file_reader = InstructionFileParser('input/' + instruction_file)
        # instr_file_reader = InstructionFileParser('input/Instruction_2.txt')
        cls.instr_file_reader.read_instructions()
        cls.instr_file_reader.print_instructions()
        print("Instruction File Parsing Done")

        print("Configuration File Parsing Started")
        cls.config_file_reader = ConfigFileParser('input/' + config_file)
        cls.config_file_reader.read_config()
        cls.config_file_reader.print_configurations()
        print("Configuration File Parsing Done")

        print("Data File Parsing Started")
        cls.data_file_reader = DataFileParser('input/' + data_file)
        cls.data_file_reader.read_memory()
        cls.data_file_reader.print_memory()
        print("Data File Parsing Done")







