from FileReader import argumentReader

class DataCache:
    block_size = argumentReader.config_file_reader.configurations.i_cache_block_size
    block_count = argumentReader.config_file_reader.configurations.i_cache_block_count

    cache_available = set()

    @classmethod
    def is_cache_available(cls, address):
        return address in cls.cache_available

    @classmethod
    def add_address_block(cls, address):
        base = address - 256
        disp = base % 16
        base = base - disp + 256

        for i in range(0,16,4):
            cls.cache_available.add(base + i)



