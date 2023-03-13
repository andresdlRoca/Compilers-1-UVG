from postfix import infix2postfix
from automatas import thompson, nfa_to_dfa
from render import automata2graph

class reg2automata:
    def __init__(self, regex:str):
        self.regex_postfix = infix2postfix(regex)
        self.regex_infix = regex
        self.nfa = None
        self.dfa = None
    
    def get_postfix(self):
        return self.regex_postfix
    
    def get_infix(self):
        return self.regex_infix

    def thompson_nfa_construction(self):
        self.nfa = thompson(self.regex_postfix)
        # print(self.nfa.states)
        # print(self.nfa.transitions)
        # print(self.nfa.alphabet)
        graph = automata2graph(self.nfa)
        graph.render('nfa', view=False)
    
    # Subconjuntos / NFA to DFA
    def nfa_to_dfa_construction(self):
        self.dfa = nfa_to_dfa(self.nfa)
        # print(self.dfa.states)
        # print(self.dfa.accept_states)
        # print(self.dfa.transitions)
        # graph = automata2graph(self.dfa)
        # graph.render('dfa', view=False)
    
    def direct_dfa(self):
        pass

    def minimization_dfa(self):
        pass

    def simulation_nfa(self, inputstring:str): #Matches a string to a regex expression
        pass
    
    def simulation_dfa(self, inputstring:str): #Matches a string to a regex expression
        pass

