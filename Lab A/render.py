import graphviz

def automata2graph(automata):
    g = graphviz.Digraph()
    epsilon = 'ε'

    # Add the states
    for state in automata.states:
        
        statestring = f'q{str(state)}'
        if state in automata.accept_states:
            g.node(statestring, shape='doublecircle')
        else:
            g.node(statestring, shape='circle')
        if state == automata.start_state:
            g.node(statestring, shape='house')

    # Add the transitions
    for (from_state, symbol), to_states in automata.transitions.items():
        fromstatestring = f'q{str(from_state)}'
        for to_state in to_states:
            tostatestring = f'q{str(to_state)}'
            if symbol == epsilon:
                g.edge(fromstatestring, tostatestring, label='ε')
            else:
                g.edge(fromstatestring, tostatestring, label=symbol)

    return g