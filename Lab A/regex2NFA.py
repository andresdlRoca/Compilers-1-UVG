from postfix import infix2Postfix

class reg2NFA:
    def __init__(self, regex:str) -> None:
        self.regex = infix2Postfix(regex)
    
    def get_regex(self):
        return self.regex