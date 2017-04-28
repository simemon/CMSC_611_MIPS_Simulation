from collections import defaultdict

class RegisterObject:
    def __init__(self):
        last_read = 0
        last_write = 0


class Register:
    def __init__(self):
        self.value = defaultdict(RegisterObject)


class Floating:
    def __init__(self):
        self.value = defaultdict(RegisterObject)