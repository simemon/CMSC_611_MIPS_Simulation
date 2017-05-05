class ICache:
    instruction_index_cache_set = set()

    @classmethod
    def add_instruction(cls, index):
        cls.instruction_index_cache_set.add(index)
