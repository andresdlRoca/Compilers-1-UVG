class automata:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

def thompson(postfix:str):
    stack = []
    state_count = 0
    transitions = {}
    epsilon = 'ε'
    alphabet = set(postfix) - set(['|', '.', '*', '(', ')'])
    for symbol in postfix:
        if symbol in alphabet:
            # Create a new automata with a single transition on this symbol
            accept_state = state_count + 1
            start_state = state_count
            state_count += 2
            if symbol == '?':
                transitions.update({(state_count-1, epsilon): [accept_state]})
            else:
                transitions.update({(start_state, symbol): [accept_state]})
            auto = automata(range(state_count), alphabet, transitions, start_state, [accept_state])
            stack.append(auto)
        elif symbol == '|':
            # Merge two automatas using union
            auto2 = stack.pop()
            auto1 = stack.pop()
            accept_state = state_count + 1
            start_state = state_count
            state_count += 2
            transitions.update({**auto1.transitions, **auto2.transitions})
            transitions.update({(start_state, epsilon): [auto1.start_state, auto2.start_state],
                                 (auto1.accept_states[0], epsilon): [accept_state],
                                 (auto2.accept_states[0], epsilon): [accept_state]})
            auto = automata(range(state_count), alphabet.union({epsilon}), transitions, start_state, [accept_state])
            stack.append(auto)
        elif symbol == '.':
            # Merge two automatas using concatenation
            auto2 = stack.pop()
            auto1 = stack.pop()
            transitions.update({**auto1.transitions, **auto2.transitions})
            transitions.update({(auto1.accept_states[0], epsilon): [auto2.start_state]})
            auto = automata(range(auto1.states[-1]+1, auto2.states[-1]+1), alphabet.union({epsilon}), transitions, auto1.start_state, [auto2.accept_states[0]])
            stack.append(auto)
        elif symbol == '*':
            # Create a new automata with a Kleene star closure
            auto1 = stack.pop()
            accept_state = state_count + 1
            start_state = state_count
            state_count += 2
            transitions = {**auto1.transitions, 
                           (start_state, epsilon): [auto1.start_state, accept_state], 
                           (auto1.accept_states[0], epsilon): [auto1.start_state, accept_state]}
            auto = automata(range(state_count), auto1.alphabet.union({epsilon}), transitions, start_state, [accept_state])
            stack.append(auto)
    
    
    last_nfa = stack.pop()
    
    transitionkeys = []
    for i in last_nfa.transitions:
        transitionkeys += i
    
    transition = {}
    for i in range(0, max(last_nfa.states) -1):
        if i not in transitionkeys:
            transition.update({(i, epsilon): [i+1]})
    
    last_nfa.transitions.update(transition)
    return last_nfa
