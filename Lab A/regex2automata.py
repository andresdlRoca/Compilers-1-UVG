from postfix import infix2postfix
from afn import NFA

class reg2automata:
    def __init__(self, regex:str) -> None:
        self.regex_postfix = infix2postfix(regex)
        self.regex_infix = regex
    
    def get_postfix(self):
        return self.regex_postfix
    
    def get_infix(self):
        return self.regex_infix

    def thompsonAFN(self):
        table = NFA()
