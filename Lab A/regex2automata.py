from postfix import infix2postfix
# from thompson import AFND
# from reader import Reader
# from render import graph_automata
# from parserautomata import Parser

class reg2automata:
    def __init__(self, regex:str) -> None:
        self.regex_postfix = infix2postfix(regex)
        self.regex_infix = regex
    
    def get_postfix(self):
        return self.regex_postfix
    
    def get_infix(self):
        return self.regex_infix

    def thompsonAFN(self):
        pass
