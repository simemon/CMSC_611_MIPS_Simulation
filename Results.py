from __future__ import print_function


class Results:
    def __init__(self):
        self.instruction = None
        self.fetch_stage = 0
        self.issue_stage = 0
        self.read_stage = 0
        self.exec_stage = 0
        self.write_stage = 0
        self.raw_hazard = 'N'
        self.waw_hazard = 'N'
        self.struct_hazard = 'N'

    def set_instruction(self, instruction):
        self.instruction = instruction

    def set_fetch_stage(self, fetch_stage):
        self.fetch_stage = fetch_stage

    def sett_issue_stage(self, issue_stage):
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

    @staticmethod
    def print_header(self):
        result = "{:<20}\t{:<5}\t{:<5}\t{:<5}\t{:<5}\t{:<5}\t{:<3}\t{:<3}\t{:<6}"
        result = result.format("INSTRUCTION", "FETCH", "ISSUE", "READ", "EXEC", "WRITE", "RAW", "WAW", "STRUCT")
        print(result)

    def print_row(self):
        result = "{:<20}\t{:<5}\t{:<5}\t{:<5}\t{:<5}\t{:<5}\t{:<3}\t{:<3}\t{:<6}"
        result = result.format(self.instruction, self.fetch_stage, self.issue_stage, self.read_stage, self.exec_stage, self.write_stage, self.raw_hazard, self.waw_hazard, self.struct_hazard)
        print(result)



