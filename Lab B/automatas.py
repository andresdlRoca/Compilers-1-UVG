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
    alphabet = set(postfix) - set(['|', '.', '*', '(', ')', '+'])
    for symbol in postfix:
        if symbol in alphabet:
            # Create a new automata with a single transition on this symbol
            if symbol == '?':
                accept_state = state_count + 1 #Node2
                start_state = state_count #Node1
                state_count += 2 
                transitions.update({(state_count, epsilon): [accept_state]})
                autooreps = automata(range(state_count), alphabet, transitions, start_state, [accept_state])
                stack.append(autooreps)
                auto2 = stack.pop()
                auto1 = stack.pop()
                transitions.update({(start_state, epsilon): [accept_state]})
                accept_state = state_count + 1
                start_state = state_count
                state_count += 2
                transitions.update({**auto1.transitions, **auto2.transitions})
                transitions.update({(start_state, epsilon): [auto1.start_state, auto2.start_state],
                                    (auto1.accept_states[0], epsilon): [accept_state],
                                    (auto2.accept_states[0], epsilon): [accept_state]})

                auto = automata(range(state_count), alphabet.union({epsilon}), transitions, start_state, [accept_state])
                stack.append(auto)
            else:
                accept_state = state_count + 1
                start_state = state_count
                state_count += 2
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
            states_diff = (auto2.states[-1]+1) - (auto1.states[-1]+1)
            state_count = (auto1.states[-1]+1) +states_diff 
            auto = automata(range(state_count), alphabet.union({epsilon}), transitions, auto1.start_state, [auto2.accept_states[0]])
            stack.append(auto)
        elif symbol == '*':
            # Create a new automata with a Kleene star closure
            auto1 = stack.pop()
            accept_state = state_count + 1
            start_state = state_count
            state_count += 2
            transitions.update({**auto1.transitions, 
                           (start_state, epsilon): [auto1.start_state, accept_state], 
                           (auto1.accept_states[0], epsilon): [auto1.start_state, accept_state]})
            auto = automata(range(state_count), auto1.alphabet.union({epsilon}), transitions, start_state, [accept_state])
            stack.append(auto)
        elif symbol == '+':
            auto1 = stack.pop() #afn1
            accept_state = state_count + 1 #Node 2
            start_state = state_count #Node 1
            state_count += 2
            transitions.update({**auto1.transitions, 
                           (start_state, epsilon): [auto1.start_state], 
                           (auto1.accept_states[0], epsilon): [auto1.start_state, accept_state]})
            auto = automata(range(state_count), auto1.alphabet.union({epsilon}), transitions, start_state, [accept_state])
            stack.append(auto)
    
    
    last_nfa = stack.pop()
    
    return last_nfa

def nfa_to_dfa(nfa:automata):
    nfa_states_array = []
    for i in nfa.states:
        nfa_states_array.append(i)
    possible_states_count = 0
    possible_states = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    created_states = {}
    alphabet = nfa.alphabet
    transitions = {}
    states = []


    # for transition in nfa.transitions:
    #     for char in alphabet:
    #         if char != nfa.transitions[transition] and nfa.transitions[transition] != "ε":
    #             nfa.alphabet.add(nfa.transitions[transition]) # NOTA: Chequear por si da error

    start_closure = eps_closure(nfa, nfa.start_state)

    created_states[possible_states[possible_states_count]] = start_closure

    for char in alphabet:
        initial_state = translate(nfa, char, start_closure)
        dest_state = eps_closure(nfa, initial_state)
        

    print(start_closure)

#Funciones que complementan a la conversion nfa -> dfa
def eps_closure(nfa, states):
    closure = []
    
    for state in range(states):
        for transition in nfa.transitions:
            if state in transition and transition[1] == "ε":
                closure.append(nfa.transitions[transition]) # Appends destination state
    
    return closure

def translate(nfa, symbol, states):
    result = []

    for state in range(states):
        for transition in nfa.transitions:
            if state in transition and transition[1] == symbol:
                result.append(nfa.transitions[transition])
    result.sort()   
    return result

def direct_dfa(postfix:str):
    pass

def minimization_dfa(dfa:automata):
    pass

