from __future__ import print_function
from Scoreboard import InstructionFileParser, ConfigFileParser, DataFileParser

print("Instruction File Parsing Started")
instr_file_reader = InstructionFileParser('input/Instr.txt')
instr_file_reader.read_instructions()
instr_file_reader.print_instructions()
print("Instruction File Parsing Done")

print("Configuration File Parsing Started")
config_file_reader = ConfigFileParser('input/Config.txt')
config_file_reader.read_config()
config_file_reader.print_configurations()
print("Configuration File Parsing Done")

print("Data File Parsing Started")
data_file_reader = DataFileParser('input/data.txt')
data_file_reader.read_memory()
data_file_reader.print_memory()
print("Data File Parsing Done")

