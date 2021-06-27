class Action:
    def __init__(self, name, description, args_dict):
        self.name = str.lower(name)
        self.description = description
        self.args_dict = args_dict

    def execute(self):
        pass

    def recognize(self, possible_name):
        if self.name == str.lower(possible_name):
            return True
        return False