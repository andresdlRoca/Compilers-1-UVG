class NFA:
    def __init__(self) -> None:
        '''
        Variables of the NFA
        '''
        self.num_states = 0
        self.start_state = 0
        self.accept_states = set()
        self.transitions = {}
    
    def add_state(self): #Adds new state to the NFA
        self.num_states += 1

    def add_transition(self, source, destination, symbol): #Adds transition to NFA according to the params
        if source not in self.transitions:
            self.transitions[source] = {}
        if symbol not in self.transitions[source]:
            self.transitions[source][symbol] = set()
        self.transitions[source][symbol].add(destination)
    
    def epsilon(self, states): 
        '''
        Calculates the epsilon closure of a set of states by doing a 
        DFS of the NFA from the input states to the epsilon transitions
        '''
        closure = set(states)
        stack = list(states)

        while stack:
            state = stack.pop()
            if state in self.transitions.get('', {}):
                for destination in self.transitions[''][state]:
                    if destination not in closure:
                        closure.add(destination)
                        stack.append(destination)
        return closure

    def move(self, states, symbol): # Calculates the set of states that can be reached from the input states of the symbol
        destination_states = set()
        for state in states:

            if state in self.transitions.get(symbol, {}):
                destination_states |= self.transitions[symbol][state]
        
        return destination_states
    

    # Thompson's construction operators

    def concat(self, other): 
        for state in self.accept_states:
            self.add_transition(state, other.start_state, '')
        self.accept_states = other.accept_states
        self.transitions.update(other.transitions)
        self.num_states += other.num_states - 1
    
    def union(self, other):
        new_start_state = self.num_states
        self.add_state()
        other_start_state = other.start_state + self.num_states
        self.add_transition(new_start_state, self.start_state, '')
        self.add_transition(new_start_state, other_start_state, '')
        self.accept_states |= {s + self.num_states for s in other.accept_states}
        self.transitions.update(other.transitions)
        self.num_states += other.num_states + 1

    def star(self):
        new_start_state = self.num_states
        self.add_state()
        self.add_transition(new_start_state, self.start_state, '')
        for state in self.accept_states:
            self.add_transition(state, self.start_state, '')
            self.add_transition(state, new_start_state, '')
        self.accept_states = {new_start_state}
        self.num_states += 1
    
    def infix2NFA(self, postfix):
        """Converts a postfix regular expression to an NFA using the Thompson construction algorithm."""
        stack = []
        for c in postfix:
            if c == '*':
                nfa = stack.pop()
                nfa.star()
                stack.append(nfa)
            elif c == '.':
                nfa2 = stack.pop()
                nfa1 = stack.pop()
                nfa1.concat(nfa2)
                stack.append(nfa1)
            elif c == '|':
                nfa2 = stack.pop()
                nfa1 = stack.pop()
                nfa1.union(nfa2)
                stack.append(nfa1)
            else:  # c is a symbol
                nfa = NFA()
                nfa.add_state()
                nfa.add_state()
                nfa.add_transition(0, 1, c)
                stack.append(nfa)
        assert len(stack) == 1
        return stack[0]
