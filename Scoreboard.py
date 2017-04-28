from __future__ import print_function

from FileReader import config_file_reader, data_file_reader, instr_file_reader
from Instruction_Type import Instruction_Adder,Instruction_Arithmetic,Instruction_Data,Instruction_Divider,Instruction_Multiplier
from Results import Results


class ScoreBoard:
    '''
    1. Read instructions one by one
    2. Check type of instruction
        3. for every instruction, perform stage by stage calculation
            4. For every stage, check hazards, update the current_stage and FU current status
    '''
    def __init__(self):
        self.instructions = instr_file_reader.instructions
        self.DATA_LIST = ["L.D", "S.D", "LW", "SW"]
        self.ARITHMETIC_LIST = ["DADD", "DADDI", "DSUB", "DSUBI", "AND", "ANDI", "OR", "ORI", "LI", "LUI"]
        self.MULTIPLIER_LIST = ["MUL.D"]
        self.ADDER_LIST = ["ADD.D", "SUB.D"]
        self.DIVIDER_LIST = ["DIV.D"]
        self.adder_count = config_file_reader.configurations.fp_adder_count
        self.adder_cycles = config_file_reader.configurations.fp_adder_cycles
        self.multiplier_count = config_file_reader.configurations.fp_multiplier_count
        self.multiplier_cycles = config_file_reader.configurations.fp_multiplier_cycles
        self.divider_count = config_file_reader.configurations.fp_divider_count
        self.divider_cycles = config_file_reader.configurations.fp_divider_cycles
        self.adder_units = []
        self.multiplier_units = []
        self.divider_units = []
        self.arithmetic_units = []
        self.data_units = []
        self.result = []

        for i in range(self.adder_count):
            self.adder_units.append(Instruction_Adder(self.adder_count, self.adder_cycles))
        for i in range(self.multiplier_count):
            self.multiplier_units.append(Instruction_Multiplier(self.multiplier_count, self.multiplier_cycles))
        for i in range(self.divider_count):
            self.divider_units.append(Instruction_Divider(self.divider_count, self.divider_cycles))
        for i in range(1):
            self.arithmetic_units.append(Instruction_Arithmetic(1, 1))
        for i in range(1):
            self.data_units.append((Instruction_Data(1,2)))

    def isAdderFree(self):
        when_available = 20000
        index_available = 0
        for index, adder in enumerate(self.adder_units):
            if adder.when_available < when_available:
                when_available = adder.when_available
                index_available = index
        return index_available, when_available

    def isMultiplierFree(self):
        for multiplier in self.multiplier_units:
            if not multiplier.isBusy:
                return True
        return False

    def isDividerFree(self):
        for divider in self.divider_units:
            if not divider.isBusy:
                return True
        return False

    def isDataFree(self):
        for data in self.data_units:
            if not data.isBusy:
                return True
        return False

    def isArithmeticFree(self):
        for arithmetic in self.arithmetic_units:
            if not arithmetic.isBusy:
                return True
        return False

    def instruction_type(self, instruction):
        if instruction.opcode in self.DATA_LIST:
            return "Data".upper()
        elif instruction.opcode in self.ARITHMETIC_LIST:
            return "Arithmetic".upper()
        elif instruction.opcode in self.MULTIPLIER_LIST:
            return "Multiplier".upper()
        elif instruction.opcode in self.ADDER_LIST:
            return "Adder".upper()
        elif instruction.opcode in self.DIVIDER_LIST:
            return "Divider".upper()
        else:
            raise "Unknown Opcode"

    def get_result(self):
        return self.result

    def execute(self):
        last_issue = 1
        for index, instruction in enumerate(self.instructions):
            current_result = Results()
            current_result.set_instruction(instruction)
            instruction_type = self.instruction_type(instruction)
            if instruction_type == "ADDER":
                # Fetch Stage
                fetch_cycle = last_issue
                current_result.set_fetch_stage(last_issue)

                #Issue Stage (WAW Pending)
                issue_cycle = fetch_cycle + 1
                index, when = self.isAdderFree()
                if when > issue_cycle:
                    current_result.set_struct_hazard('Y')
                    issue_cycle = when + 1
                current_result.set_issue_stage(issue_cycle)
                last_issue = issue_cycle

                #Read Stage (RAW Pending)
                '''
                if raw_hazard()
                    then wait
                else
                    use issue_cycle + 1
                '''
                read_cycle = issue_cycle + 1
                current_result.set_read_stage(read_cycle)

                #Exec Stage
                exec_cycle = read_cycle + self.adder_cycles
                current_result.set_exec_stage(exec_cycle)

                #Write Back Stage
                write_cycle = exec_cycle + 1
                current_result.set_write_stage(write_cycle)
                self.adder_units[index].when_available = write_cycle


            self.result.append(current_result)


















