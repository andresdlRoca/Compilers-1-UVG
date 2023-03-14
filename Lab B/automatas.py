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
    alphabet = sorted(nfa.alphabet)
    transitions = {}
    states = []
    unmarked_states = []

    # for transition in nfa.transitions:
    #     for char in alphabet:
    #         if char != nfa.transitions[transition] and nfa.transitions[transition] != "ε":
    #             nfa.alphabet.add(nfa.transitions[transition]) # NOTA: Chequear por si da error

    start_closure = eps_closure(nfa, nfa.start_state)
    states.append(start_closure)
    created_states[possible_states[possible_states_count]] = start_closure
    for char in alphabet:
        initial_state = translate(nfa, char, start_closure)
        dest_state = eps_closure(nfa, initial_state)
        # print(initial_state)
        # print(dest_state)
        # print(char)
        for i in initial_state:
            for state in i:
                transitions[(state, char)] = dest_state

        if dest_state not in states:
            states.append(dest_state)
            possible_states_count += 1
            created_states[possible_states[possible_states_count]] = dest_state

    print('transitions', transitions)
    print('created_states', created_states)

    # unmarked_states.append(start_closure)

    # for state in states:
    #     if state not in unmarked_states:
    #         unmarked_states.append(state)
    #         for char in alphabet:
    #             initial_state = translate(nfa, char, state)
    #             dest_state = eps_closure(nfa, initial_state)
    #             for i in initial_state:
    #                 for x_state in i:
    #                     transitions[(x_state, char)] = dest_state

    #             if dest_state not in states:
    #                 states.append(dest_state)
    #                 possible_states_count += 1
    #                 created_states[possible_states[possible_states_count]] = dest_state
    
    # print(created_states)
    # print(transitions)
    # resulting_transitions = {}
    # # print(transitions)
    # for transition in transitions:
    #     initial_state = ''
    #     dest_state = ''
    #     for llave, valor in created_states.items():
    #         # print("Valor", valor)
    #         # print("Transition", transition)
    #         if [transition[0]] in valor:
    #             initial_state = llave
    #     for llave,valor in created_states.items():
    #         if valor == transitions[transition]:
    #             dest_state = llave
    #     char = transition[1]

    #     # print(initial_state)
    #     # print(dest_state)
    #     resulting_transitions[(initial_state, char)] = dest_state
    
    # print(resulting_transitions)
        


    

#Funciones que complementan a la conversion nfa -> dfa
def eps_closure(nfa, states):
    closure = []
    state_result = []
    state_array = []

    try:
        for state in states:
            state_result.append(state)
            state_array.append(state)
        
        for state in state_array:
            for transition in nfa.transitions:
                if transition[1] == 'ε':
                    state_array.append(nfa.transitions[transition])
                    state_result.append(nfa.transitions[transition])
                else:
                    pass
        
        return state_result
    except:
        for state in range(states):
            state_result.append(state)
            state_array.append(state)
        
        for state in state_array:
            print(state_array)
            for transition in nfa.transitions:

                if transition[1] == 'ε' and state in transition:
                    state_array.append(nfa.transitions[transition])
                    state_result.append(nfa.transitions[transition])
                else:
                    pass
        
        return state_result

def translate(nfa, symbol, states):
    result = []

    for state in states:
        for transition in nfa.transitions:
            if transition[1] == symbol and state in transition:
                result.append(nfa.transitions[transition])
            else:
                pass
    
    return result

def direct_dfa(postfix:str):
    pass

def minimization_dfa(dfa:automata):
    pass

