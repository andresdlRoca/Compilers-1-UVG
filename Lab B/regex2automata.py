from postfix import infix2postfix
from automatas import thompson
from render import automata2graph

class reg2automata:
    def __init__(self, regex:str):
        self.regex_postfix = infix2postfix(regex)
        self.regex_infix = regex
        self.nfa = None
    
    def get_postfix(self):
        return self.regex_postfix
    
    def get_infix(self):
        return self.regex_infix

    def thompson_nfa_construction(self):
        self.nfa = thompson(self.regex_postfix)
        graph = automata2graph(self.nfa)
        graph.render('nfa', view=True)
    
    def matching(self, inputstring:str): #Matches a string to a regex expression
        pass

