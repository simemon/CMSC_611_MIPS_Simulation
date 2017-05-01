from __future__ import print_function


class Results:
    def __init__(self):
        self.current_stage = 'INIT'
        self.current_stage_count = 0
        # Instruction Type: unconditional,conditional,special,data,arithmetic,adder,multiply,division
        self.instruction_type = None
        self.instruction = None
        self.fetch_stage = 0
        self.issue_stage = 0
        self.read_stage = 0
        self.exec_stage = 0
        self.write_stage = 0
        self.raw_hazard = 'N'
        self.waw_hazard = 'N'
        self.struct_hazard = 'N'
        self.instruction_text = ""

    def set_instruction(self, instruction):
        self.instruction = instruction
        self.instruction_text = instruction.text

    def set_fetch_stage(self, fetch_stage):
        self.fetch_stage = fetch_stage

    def set_issue_stage(self, issue_stage):
        self.issue_stage = issue_stage

    def set_read_stage(self, read_stage):
        self.read_stage = read_stage

    def set_exec_stage(self, exec_stage):
        self.exec_stage = exec_stage

    def set_write_stage(self, write_stage):
        self.write_stage = write_stage

    def set_raw_hazard(self, raw_hazard):
        self.raw_hazard = raw_hazard

    def set_waw_hazard(self, waw_hazard):
        self.waw_hazard = waw_hazard

    def set_struct_hazard(self, struct_hazard):
        self.struct_hazard = struct_hazard

    @classmethod
    def print_header(cls):
        result = "{:<20}\t{:<5}\t{:<5}\t{:<5}\t{:<5}\t{:<5}\t{:<3}\t{:<3}\t{:<6}"
        result = result.format("INSTRUCTION", "FETCH", "ISSUE", "READ", "EXEC", "WRITE", "RAW", "WAW", "STRUCT")
        print(result)

    def print_row(self):
        result = "{text:<20}\t{fetch:<5}\t{issue:<5}\t{read:<5}\t{executable:<5}\t{write:<5}\t{raw:<3}\t{waw:<3}\t{struct:<6}"
        result = result.format(text=self.instruction_text, fetch=self.fetch_stage, issue=self.issue_stage, read = self.read_stage if self.read_stage != 0 else "-", executable=self.exec_stage if self.exec_stage != 0 else "-", write = self.write_stage if self.write_stage != 0 else "-", raw=self.raw_hazard, waw=self.waw_hazard, struct=self.struct_hazard)
        print(result)



