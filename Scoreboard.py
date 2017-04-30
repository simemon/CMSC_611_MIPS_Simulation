from __future__ import print_function

from FileReader import config_file_reader, data_file_reader, instr_file_reader
from Instruction_Type import Instruction_Adder,Instruction_Arithmetic,Instruction_Data,Instruction_Divider,Instruction_Multiplier
from Results import Results
from Storage import RegisterObject, Register, Floating
from Data import Memory

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
        self.arithmetic_count = config_file_reader.configurations.arithmetic_count
        self.arithmetic_cycles = config_file_reader.configurations.arithmetic_cycles
        self.data_count = config_file_reader.configurations.data_count
        self.data_cycles = config_file_reader.configurations.data_cycles
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
        when_available = 20000
        index_available = 0
        for index, multiplier in enumerate(self.multiplier_units):
            if multiplier.when_available < when_available:
                when_available = multiplier.when_available
                index_available = index
        return index_available, when_available

    def isDividerFree(self):
        when_available = 20000
        index_available = 0
        for index, divider in enumerate(self.divider_units):
            if divider.when_available < when_available:
                when_available = divider.when_available
                index_available = index
        return index_available, when_available

    def isDataFree(self):
        when_available = 20000
        index_available = 0
        for index, data in enumerate(self.data_units):
            if data.when_available < when_available:
                when_available = data.when_available
                index_available = index
        return index_available, when_available

    def isArithmeticFree(self):
        when_available = 20000
        index_available = 0
        for index, arithmetic in enumerate(self.arithmetic_units):
            if arithmetic.when_available < when_available:
                when_available = arithmetic.when_available
                index_available = index
        return index_available, when_available

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

    def parse_instruction(self, instruction):
        if instruction.opcode == "LI":
            if instruction.dest_register[0] not  in Register.value:
                Register.value[instruction.dest_register[0]] = RegisterObject()
            Register.value[instruction.dest_register[0]].value = int(instruction.source_register[0])

        elif instruction.opcode == "L.D":
            if instruction.dest_register[0] not  in Floating.value:
                Floating.value[instruction.dest_register[0]] = RegisterObject()
            base = Register.value[instruction.source_register[0]].value
            base += instruction.displacement
            base = data_file_reader.memory.get_value(base)
            Floating.value[instruction.dest_register[0]].value = base

        elif instruction.opcode == "DADDI":
            if instruction.dest_register[0] not  in Register.value:
                Register.value[instruction.dest_register[0]] = RegisterObject()
            if instruction.source_register[0] not  in Register.value:
                Register.value[instruction.source_register[0]] = RegisterObject()

            calc = Register.value[instruction.source_register[0]].value
            calc += int(instruction.source_register[1])
            Register.value[instruction.dest_register[0]].value = calc

        elif instruction.opcode == "DSUBI":
            if instruction.dest_register[0] not  in Register.value:
                Register.value[instruction.dest_register[0]] = RegisterObject()
            if instruction.source_register[0] not  in Register.value:
                Register.value[instruction.source_register[0]] = RegisterObject()

            calc = Register.value[instruction.source_register[0]].value
            calc -= int(instruction.source_register[1])
            Register.value[instruction.dest_register[0]].value = calc

        elif instruction.opcode == "DADD":
            if instruction.dest_register[0] not  in Register.value:
                Register.value[instruction.dest_register[0]] = RegisterObject()
            for register in instruction.source_register:
                if register not in Register.value:
                    Register.value[register] = RegisterObject()

            calc = Register.value[instruction.source_register[0]].value
            calc += Register.value[instruction.source_register[1]].value
            Floating.value[instruction.dest_register[0]].value = calc

        elif instruction.opcode == "DSUB":
            if instruction.dest_register[0] not  in Register.value:
                Register.value[instruction.dest_register[0]] = RegisterObject()
            for register in instruction.source_register:
                if register not in Register.value:
                    Register.value[register] = RegisterObject()

            calc = Register.value[instruction.source_register[0]].value
            calc -= Register.value[instruction.source_register[1]].value
            Floating.value[instruction.dest_register[0]].value = calc

        elif instruction.opcode == "ADD.D":
            if instruction.dest_register[0] not  in Floating.value:
                Floating.value[instruction.dest_register[0]] = RegisterObject()
            for register in instruction.source_register:
                if register not in Floating.value:
                    Floating.value[register] = RegisterObject()

            calc = Floating.value[instruction.source_register[0]].value
            calc += Floating.value[instruction.source_register[1]].value
            Floating.value[instruction.dest_register[0]].value = calc

        elif instruction.opcode == "SUB.D":
            if instruction.dest_register[0] not  in Floating.value:
                Floating.value[instruction.dest_register[0]] = RegisterObject()
            for register in instruction.source_register:
                if register not in Floating.value:
                    Floating.value[register] = RegisterObject()

            calc = Floating.value[instruction.source_register[0]].value
            calc -= Floating.value[instruction.source_register[1]].value
            Floating.value[instruction.dest_register[0]].value = calc

        elif instruction.opcode == "MULT.D":
            if instruction.dest_register[0] not  in Floating.value:
                Floating.value[instruction.dest_register[0]] = RegisterObject()
            for register in instruction.source_register:
                if register not in Floating.value:
                    Floating.value[register] = RegisterObject()

            calc = Floating.value[instruction.source_register[0]].value
            calc *= Floating.value[instruction.source_register[1]].value
            Floating.value[instruction.dest_register[0]].value = calc

        elif instruction.opcode == "DIV.D":
            if instruction.dest_register[0] not  in Floating.value:
                Floating.value[instruction.dest_register[0]] = RegisterObject()
            for register in instruction.source_register:
                if register not in Floating.value:
                    Floating.value[register] = RegisterObject()

            param1 = Floating.value[instruction.source_register[0]].value
            param2 = Floating.value[instruction.source_register[1]].value
            param1 = param1 // param2 if param2 != 0 else param1
            Floating.value[instruction.dest_register[0]].value = param1


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

                # Parsing Instruction to update the memory
                self.parse_instruction(instruction)

                #Issue Stage
                issue_cycle = fetch_cycle + 1
                index, when = self.isAdderFree()
                if when > issue_cycle:
                    current_result.set_struct_hazard('Y')
                    issue_cycle = when + 1

                temp_cycle = issue_cycle
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                if temp_cycle > issue_cycle:
                    current_result.set_waw_hazard('Y')

                issue_cycle = temp_cycle
                current_result.set_issue_stage(issue_cycle)
                last_issue = issue_cycle

                #Read Stage
                read_cycle = issue_cycle + 1
                temp_cycle = read_cycle

                #Handling RAW Hazards (Source)
                for register in instruction.source_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                #Handling RAW Hazards (Destination)
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)
                    temp_cycle = max(Register.value[register].last_read + 1, temp_cycle)

                if temp_cycle > read_cycle:
                    current_result.set_raw_hazard('Y')

                read_cycle = temp_cycle
                current_result.set_read_stage(read_cycle)

                #Exec Stage
                exec_cycle = read_cycle + self.adder_cycles
                current_result.set_exec_stage(exec_cycle)

                #Write Back Stage
                write_cycle = exec_cycle + 1
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    Register.value[register].last_write = write_cycle

                current_result.set_write_stage(write_cycle)
                self.adder_units[index].when_available = write_cycle

            elif instruction_type == "DATA":
                # Fetch Stage
                fetch_cycle = last_issue
                current_result.set_fetch_stage(last_issue)

                # Parsing Instruction to update the memory
                self.parse_instruction(instruction)

                #Issue Stage (WAW Pending)
                issue_cycle = fetch_cycle + 1
                index, when = self.isDataFree()
                if when > issue_cycle:
                    current_result.set_struct_hazard('Y')
                    issue_cycle = when + 1

                temp_cycle = issue_cycle
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                if temp_cycle > issue_cycle:
                    current_result.set_waw_hazard('Y')

                issue_cycle = temp_cycle
                current_result.set_issue_stage(issue_cycle)
                last_issue = issue_cycle

                #Read Stage
                read_cycle = issue_cycle + 1
                temp_cycle = read_cycle

                #Handling RAW Hazards (Source)
                for register in instruction.source_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                #Handling RAW Hazards (Destination)
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)
                    temp_cycle = max(Register.value[register].last_read + 1, temp_cycle)

                if temp_cycle > read_cycle:
                    current_result.set_raw_hazard('Y')

                read_cycle = temp_cycle
                current_result.set_read_stage(read_cycle)

                #Exec Stage
                exec_cycle = read_cycle + self.data_cycles
                current_result.set_exec_stage(exec_cycle)

                #Write Back Stage
                write_cycle = exec_cycle + 1
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    Register.value[register].last_write = write_cycle

                current_result.set_write_stage(write_cycle)
                self.data_units[index].when_available = write_cycle

            elif instruction_type == "ARITHMETIC":
                # Fetch Stage
                fetch_cycle = last_issue
                current_result.set_fetch_stage(last_issue)

                # Parsing Instruction to update the memory
                self.parse_instruction(instruction)

                #Issue Stage (WAW Pending)
                issue_cycle = fetch_cycle + 1
                index, when = self.isArithmeticFree()
                if when > issue_cycle:
                    current_result.set_struct_hazard('Y')
                    issue_cycle = when + 1

                temp_cycle = issue_cycle
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                if temp_cycle > issue_cycle:
                    current_result.set_waw_hazard('Y')

                issue_cycle = temp_cycle
                current_result.set_issue_stage(issue_cycle)
                last_issue = issue_cycle

                #Read Stage
                read_cycle = issue_cycle + 1
                temp_cycle = read_cycle

                #Handling RAW Hazards (Source)
                for register in instruction.source_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                #Handling RAW Hazards (Destination)
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)
                    temp_cycle = max(Register.value[register].last_read + 1, temp_cycle)

                if temp_cycle > read_cycle:
                    current_result.set_raw_hazard('Y')

                read_cycle = temp_cycle
                current_result.set_read_stage(read_cycle)

                #Exec Stage
                exec_cycle = read_cycle + self.arithmetic_cycles
                current_result.set_exec_stage(exec_cycle)

                #Write Back Stage
                write_cycle = exec_cycle + 1
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    Register.value[register].last_write = write_cycle

                current_result.set_write_stage(write_cycle)
                self.arithmetic_units[index].when_available = write_cycle

            elif instruction_type == "MULTIPLIER":
                # Fetch Stage
                fetch_cycle = last_issue
                current_result.set_fetch_stage(last_issue)

                # Parsing Instruction to update the memory
                self.parse_instruction(instruction)

                #Issue Stage (WAW Pending)
                issue_cycle = fetch_cycle + 1
                index, when = self.isMultiplierFree()
                if when > issue_cycle:
                    current_result.set_struct_hazard('Y')
                    issue_cycle = when + 1

                temp_cycle = issue_cycle
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                if temp_cycle > issue_cycle:
                    current_result.set_waw_hazard('Y')

                issue_cycle = temp_cycle
                current_result.set_issue_stage(issue_cycle)
                last_issue = issue_cycle

                #Read Stage
                read_cycle = issue_cycle + 1
                temp_cycle = read_cycle

                #Handling RAW Hazards (Source)
                for register in instruction.source_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                #Handling RAW Hazards (Destination)
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)
                    temp_cycle = max(Register.value[register].last_read + 1, temp_cycle)

                if temp_cycle > read_cycle:
                    current_result.set_raw_hazard('Y')

                read_cycle = temp_cycle
                current_result.set_read_stage(read_cycle)

                #Exec Stage
                exec_cycle = read_cycle + self.multiplier_cycles
                current_result.set_exec_stage(exec_cycle)

                #Write Back Stage
                write_cycle = exec_cycle + 1
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    Register.value[register].last_write = write_cycle

                current_result.set_write_stage(write_cycle)
                self.multiplier_units[index].when_available = write_cycle

            elif instruction_type == "DIVIDER":
                # Fetch Stage
                fetch_cycle = last_issue
                current_result.set_fetch_stage(last_issue)

                # Parsing Instruction to update the memory
                self.parse_instruction(instruction)

                # Issue Stage (WAW Pending)
                issue_cycle = fetch_cycle + 1
                index, when = self.isDividerFree()
                if when > issue_cycle:
                    current_result.set_struct_hazard('Y')
                    issue_cycle = when + 1

                temp_cycle = issue_cycle
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                if temp_cycle > issue_cycle:
                    current_result.set_waw_hazard('Y')

                issue_cycle = temp_cycle
                current_result.set_issue_stage(issue_cycle)
                last_issue = issue_cycle

                #Read Stage
                read_cycle = issue_cycle + 1
                temp_cycle = read_cycle

                #Handling RAW Hazards (Source)
                for register in instruction.source_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)

                #Handling RAW Hazards (Destination)
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    temp_cycle = max(Register.value[register].last_write + 1, temp_cycle)
                    temp_cycle = max(Register.value[register].last_read + 1, temp_cycle)

                if temp_cycle > read_cycle:
                    current_result.set_raw_hazard('Y')

                read_cycle = temp_cycle
                current_result.set_read_stage(read_cycle)

                #Exec Stage
                exec_cycle = read_cycle + self.divider_cycles
                current_result.set_exec_stage(exec_cycle)

                #Write Back Stage
                write_cycle = exec_cycle + 1
                for register in instruction.dest_register:
                    if register not in Register.value:
                        Register.value[register] = RegisterObject()
                    Register.value[register].last_write = write_cycle

                current_result.set_write_stage(write_cycle)
                self.divider_units[index].when_available = write_cycle

            self.result.append(current_result)


















