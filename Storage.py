from collections import defaultdict


class RegisterObject:

    def __init__(self):
        self.last_read = 0
        self.last_write = 0


class Register:
    value = defaultdict(RegisterObject)

    def __init__(self):
        pass


class Floating:
    value = defaultdict(RegisterObject)

    def __init__(self):
        pass