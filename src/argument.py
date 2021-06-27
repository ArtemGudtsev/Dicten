class Argument:
    def __init__(self, name, description, has_param=False, required=False):
        self.name = name
        self.description = description
        self.has_param = has_param
        self.required = required
